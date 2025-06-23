from sqlalchemy import func, desc
from collections import defaultdict

# 年龄分布
def getPieData(records):
    Age_Dic = {
        '0-10岁': 0,
        '10-20岁': 0,
        '20-30岁': 0,
        '30-40岁': 0,
        '40-50岁': 0,
        '50-60岁': 0,
        '60岁以上': 0
    }
    for record in records:
        age = int(record.Patient_Age)
        if age <= 10:
            Age_Dic['0-10岁'] += 1
        elif age <= 20:
            Age_Dic['10-20岁'] += 1
        elif age <= 30:
            Age_Dic['20-30岁'] += 1
        elif age <= 40:
            Age_Dic['30-40岁'] += 1
        elif age <= 50:
            Age_Dic['40-50岁'] += 1
        elif age <= 60:
            Age_Dic['50-60岁'] += 1
        else:
            Age_Dic['60岁以上'] += 1
    Age_list = []
    for k,v in Age_Dic.items():
        Age_list.append({
            'name': k,
            'value': v
        })
    return Age_list

# 疾病类型统计
def get_Disease_type(records):
    Disease_Type_Dic = {}
    for record in records:
        if not Disease_Type_Dic.get(record.Disease_type):
            Disease_Type_Dic[record.Disease_type] = 1
        else:
            Disease_Type_Dic[record.Disease_type] += 1
    Disease_Type_List = []
    for k,v in Disease_Type_Dic.items():
        Disease_Type_List.append({
            'name': k,
            'value': v
        })
    return Disease_Type_List

# 疾病队列
def get_Lines(records):
    Lines_List = []
    count = 0
    while count <= 100:
        for record in records:
            Disease_type = record.Disease_type
            Patient_Gender = record.Patient_Gender
            Patient_Age = record.Patient_Age
            Patient_Height = record.Patient_Height
            Patient_Weight = record.Patient_Weight
            Allergy_history = record.Allergy_history
            Department = record.Department
            Case_record = [
                Disease_type,
                Department,
                Patient_Gender,
                Patient_Age,
                Patient_Height,
                Patient_Weight,
                Allergy_history,
            ]
            Lines_List.append(Case_record)
            count += 1
    return Lines_List

# 中间数据统计
def get_most_common(session, column):
    return (
        session.query(column, func.count(column).label("count"))
        .group_by(column)
        .order_by(func.count(column).desc())
        .first()
    )

def center_summary(session,records,databases):
    data_num = len(records)
    result = session.query(
        func.max(databases.Patient_Age),
        func.min(databases.Patient_Age),
    ).one()
    max_age,min_age = result
    max_type = get_most_common(session, databases.Disease_type)[0]
    max_department = get_most_common(session, databases.Department)[0]
    max_hospital = get_most_common(session, databases.Hospital)[0]
    return [data_num, max_type, max_department, max_age, min_age, max_hospital]
    
# 男女患病对比
def Comparision_Gender(session, databases):
    # 按性别 + 疾病种类统计数量
    result = session.query(
        databases.Patient_Gender,
        databases.Disease_type,
        func.count().label('count')
    ).group_by(
        databases.Patient_Gender,
        databases.Disease_type
    ).all()

    man_prop_lst = []
    woman_prop_lst = []
    woman_counts = 0
    man_counts = 0
    for gender, disease, count in result:
        if gender == '女':
            woman_counts += 1
            woman_prop_lst.append({
                'name': disease,
                'value': count
            })
        else:
            man_counts += 1
            man_prop_lst.append({
                'name': disease,
                'value': count
            })
    gender_ratio = [int(man_counts/(man_counts + woman_counts)*100)]
    return man_prop_lst,woman_prop_lst,gender_ratio

# 挂号科室统计，只丢8个部门进去
def Department_Summary(records):
    Department_Dic = {}
    Department_List = []
    count = 0
    for record in records:
        Department = record.Department
        if Department_Dic.get(Department):
            Department_Dic[Department] += 1
        else:
            Department_Dic[Department] = 1
    for key,value in Department_Dic.items():
        Department_List.append({
            'name': key,
            'value': value
        })

    return Department_List

# 微信词云
def Worddat(records):
    Word_Dic = {}
    Word_List = []
    for record in records:
        Disease_type = record.Disease_type
        if Word_Dic.get(Disease_type):
            Word_Dic[Disease_type] += 1
        else:
            Word_Dic[Disease_type] = 1
    for k,v in Word_Dic.items():
        Word_List.append({
            'name': k,
            'value': v
        })
    return Word_List

# 获取平均身高、体重
def Avg_height_weight(records):
    # 按照每个疾病类型分类
    average_height_dic = defaultdict(list)
    average_weight_dic = defaultdict(list)
    for record in records:
        Disease_type = record.Disease_type
        if average_height_dic.get(Disease_type):
            average_height_dic[Disease_type][0] += record.Patient_Height
            average_height_dic[Disease_type][1] += 1
            average_weight_dic[Disease_type][0] += record.Patient_Weight
            average_weight_dic[Disease_type][1] += 1
        else:
            average_height_dic[Disease_type].extend([record.Patient_Height,1])
            average_weight_dic[Disease_type].extend([record.Patient_Weight,1])
    Disease_type_list = []
    average_height_list = []
    average_weight_list = []
    for k,v in average_height_dic.items():
        avg_v = int(v[0]/v[1])
        Disease_type_list.append(k)
        average_height_list.append(avg_v)
    for k,v in average_weight_dic.items():
        avg_v = round(v[0]/v[1],2)
        average_weight_list.append(avg_v)
    return Disease_type_list,average_height_list,average_weight_list
