import requests
from lxml import etree
import pandas as pd
import re
from sqlalchemy import create_engine
from models import Medical_database,Medical,get_engine
from sqlalchemy.orm import sessionmaker
import json
import time
from collections import defaultdict
import random


class spider(object):
    def __init__(self):
        self.header = {
          "..."
        }

    def init_database(self):
        self.engine = get_engine()
        Medical.metadata.create_all(self.engine)
        return self.engine

    def spider_main(self, url, page_index):
        custumor_detail = defaultdict(list)
        patients_counts = 0

        # 解析主页
        html = requests.get(url, headers=self.header).text
        time.sleep(0.5)
        html = etree.HTML(html)
        
        # 跳转特定疾病网址
        for li_type in html.xpath('//*[@id="searchdoctor"]/div[2]/div[2]/ul/li'):
            li_type_href = f"https:{li_type.xpath('./a/@href')[0]}?page={page_index}"
            li_type_href = re.sub(r'tuijian-doctor\.html', 'bingcheng.html', li_type_href)

            Disease_type = li_type.xpath('./a/text()')[0]
            Disease_html = requests.get(li_type_href, headers=self.header).text
            time.sleep(0.3)
            Disease_html = etree.HTML(Disease_html)
            
            # 所属疾病患者列表
            for li in Disease_html.xpath('//*[@id="me-content"]/main/section/div/ul/li'):
                print("爬取第%s条数据。。。"%patients_counts)

                # 患者信息
                li_span_detail = li.xpath('./a/div/span[1]/text()')
                Patient_Gender = li_span_detail[0].split('：')[1].split(' ')[0]
                Patient_Age = li_span_detail[0].split('：')[1].split(' ')[-1].split('岁')[0]
                Consultation_time = li.xpath('./a/div/span[@class="date"]/text()')[0]
                Description = li.xpath('./a/h3/text()')[0]
                Doctor = li.xpath('./div/div[2]/a[1]/text()')[0]
                Hospital = li.xpath('./div/div[2]/a[2]/text()')[0]
                Department = li.xpath('./div/div[2]/a[3]/text()')[0]
                Detail_link = li.xpath("./a/@href")[0]

                # 详细页解析
                Patient_Height = '无'
                Patient_Weight = '无'
                Time_of_illness = '无'
                Allergy_history = '无'
                try:
                    detail_html = requests.get(Detail_link, headers=self.header).text                 
                    detail_html = etree.HTML(detail_html)
                    spans_nums = len(detail_html.xpath('/html/body/main/section/p/span'))
                    
                    for index in range(spans_nums):
                        try:
                            span_detail = detail_html.xpath('/html/body/main/section/p/span[%d]/text()'%index)[0]
                            if re.match(r"身高体重",span_detail):
                                span_detail_2 = detail_html.xpath('/html/body/main/section/p/span[%d]/text()'%(index+1))[0]
                                Patient_Height = span_detail_2.split("，")[0].split('cm')[0]
                                Patient_Weight = span_detail_2.split("，")[1].split('kg')[0]
                            elif re.match(r"患病时长",span_detail):
                                Time_of_illness = detail_html.xpath('/html/body/main/section/p/span[%d]/text()'%(index+1))[0]
                            elif re.match(r"过敏史", span_detail):
                                Allergy_history = detail_html.xpath('/html/body/main/section/p/span[%d]/text()'%(index+1))[0].split('(')[0]
                        except:
                            pass
                except:
                    interval = round(random.uniform(0,1),4)
                    time.sleep(interval)
                    print("第%s条数据爬取失败"%patients_counts)
                custumor_detail[patients_counts] = [
                        Disease_type,
                        Patient_Gender,
                        Patient_Age,
                        Patient_Height,
                        Patient_Weight,
                        Time_of_illness,
                        Allergy_history,
                        Consultation_time,
                        Description,
                        Doctor,
                        Hospital,
                        Department,
                        Detail_link,
                    ]
                patients_counts += 1
        return custumor_detail

if __name__ == "__main__":
    SpiderObj = spider()
    engine = SpiderObj.init_database()

    Spider_url = 'https://www.haodf.com/'
    # 写入数据库
    # 创建会话
    Session = sessionmaker(bind=engine)
    session = Session()
    custumor_info_lst = []
    field_names = [
        "Disease_type",
        "Patient_Gender",
        "Patient_Age",
        "Patient_Height",
        "Patient_Weight",
        "Time_of_illness",
        "Allergy_history",
        "Consultation_time",
        "Description",
        "Doctor",
        "Hospital",
        "Department",
        "Detail_link",
    ]
    
    for page_index in range(3):
        custumor_detail = SpiderObj.spider_main(Spider_url, page_index)
        # 由于第一个参数设置为数据库中的ID index默认参数，所以需要跳过，不能使用*args，转而使用**kargs具体参数。
        for key,value_lst in custumor_detail.items():
            print(value_lst)
            data_dict = dict(zip(field_names, value_lst)) 
            custumor_info = Medical_database(**data_dict)
            custumor_info_lst.append(custumor_info)
            # 传入列表要用add_all
        session.add_all(custumor_info_lst)
        session.commit()


# 在数据库中更换数据信息
all_records = session.query(Medical_database).all()
for record in all_records:
    if record.Patient_Height == '无':
        record.Patient_Height = str(random.randint(150, 190))
    if record.Patient_Weight == '无':
        record.Patient_Weight =  str(round(random.uniform(80,200),2))
session.commit()