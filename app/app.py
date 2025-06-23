from flask import Flask,request,session,g,jsonify
from flask_migrate import Migrate
from script.models import get_session,Medical_database
from script.getData import *
from script.machine import *

app = Flask(__name__)

@app.route('/')
def main():
    return "hello world！"

@app.route('/getHomedata',methods=['GET','POST'])
def gethomedata():
    session = get_session()
    try:
        Medical_records = session.query(Medical_database).all()
        pieData = getPieData(Medical_records)
        Disease_type_data = get_Disease_type(Medical_records)
        Lines_List = get_Lines(Medical_records)
        Center_Display = center_summary(session, Medical_records, Medical_database)
        man_prop_lst,woman_prop_lst,gender_ratio = Comparision_Gender(session, Medical_database)
        department = Department_Summary(Medical_records)
        Wordset = Worddat(Medical_records)
        xData,yData1,yData2= Avg_height_weight(Medical_records)
        return jsonify({
            'message': 'success',
            'code': 200,
            'data':{
                'pieData': pieData,
                'Disease_type_data': Disease_type_data,
                'Center_Display': Center_Display,
                'Lines': Lines_List,
                'man_prop': man_prop_lst,
                'woman_prop': woman_prop_lst,
                'gender_ratio': gender_ratio,
                'Department_Summary': department,
                'Wordset': Wordset,
                'Average_chart': {"xData":xData,"yData1":yData1,"yData2":yData2}
            }
        })
    finally:
        session.close()

@app.route('/getPred',methods=['GET','POST'])
def getPred():
    if request.method == 'POST':
        text_dic = request.get_json()
        for k,v in text_dic.items():
            text = v
        session = get_session()
        try:
            Medical_records = session.query(Medical_database).all()
            # 导入模型，可以本地化导入文件，这样便于读取，变成全局变量，免得数据库过大导致网站加载过慢，和每次访问开启模型预测问题。我这么写懒得改了😊。样本太少了，模型预测的稀烂😀。
            model = train_model(Medical_records)
            stopwords = get_stopword()
            words = [w for w in jieba.cut(text) if w not in stopwords]
            clean_text = ' '.join(words)
            # 特征向量
            vector = vectorizer.transform([clean_text])
            predic_result = model.predict(vector)
            print(clean_text)
            return jsonify({"prediction": predic_result[0]})
        finally:
            session.close()

@app.route('/getTable',methods=['GET','POST'])
def getTable():
    session = get_session()
    try:
        Medical_records = session.query(Medical_database).all()
        Lines_List = get_Lines(Medical_records)
        return jsonify({
            'message': 'success',
            'code': 200,
            'data':{
                'Lines_List': Lines_List
            }
        })
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)

