import jieba
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
from pathlib import Path

def get_stopword():
    current_dir = Path(__file__).parent
    stopwordfile = current_dir.parent / "stopword.txt"
    stopwords = set(open(stopwordfile, 'r', encoding='utf-8').read().splitlines())
    return stopwords

def tokensize(text):
    stopwords = get_stopword()
    words = [word for word in jieba.cut(text) if word not in stopwords]
    return ' '.join(words) # 这里返回的是X特征，代表疾病类型的综合特征

# 分词得到特征和标签数据
def machine_Data(records):
    charact_lst = []
    lable_lst = []
    for record in records:
        charact_lst.append(tokensize(record.Description))
        lable_lst.append(record.Disease_type)
    return charact_lst,lable_lst


# 设置最大特征数目，通过CountVectorizer 生成词频矩阵。
vectorizer = TfidfVectorizer(max_features=1000)
# 模型训练
def train_model(records): 
    charact_lst,lable_lst = machine_Data(records)

    # train_test_split函数将X,Y分割成训练集，验证集。
    x_train,x_test,y_train,y_test = train_test_split(charact_lst,lable_lst,test_size=0.3,random_state=52)

    # 训练集上拟合向量化器
    x_train_vectorized = vectorizer.fit_transform(x_train)  # 学习词汇表并计算TF-IDF
    # 测试集仅做转换（使用训练集的统计量）
    x_test_vectorized = vectorizer.transform(x_test)

    # 模型训练，随机森林算法，随机森林可以理解为多个决策树组成。
    model = RandomForestClassifier(n_estimators=100,random_state=52)
    model.fit(x_train_vectorized,y_train)   
    # 计算准确性，数据太少了，模型预测没啥用
    # y_pred = model.predict()
    # accuracy = accuracy_score(y_pred,y_test)
    # print(accuracy)
    return model