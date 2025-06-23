from sqlalchemy import create_engine,Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import yaml
from pathlib import Path
from sqlalchemy.orm import sessionmaker

# 导入配置
def load_config():
    # 获取当前文件的父目录
    current_dir = Path(__file__).parent
    config_path = current_dir.parent / "config.yaml"
    with open(config_path, 'r', encoding='utf-8') as f:
        config_yaml = yaml.load(f, Loader=yaml.FullLoader)
    return config_yaml

# 获取引擎
def get_engine():
    config_file = load_config()
    HOSTNAME = config_file['HOSTNAME']
    POST = config_file['POST']
    USERNAME = config_file['USERNAME']
    PASSWORD = config_file['PASSWORD']
    DATABASE = config_file['DATABASE']
    engine = f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{POST}/{DATABASE}'
    return create_engine(engine)

# 连接数据库，返回对话对象
def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

# 创建基类
Medical = declarative_base()

# 疾病名称、性别、患者年龄、问诊时间、描述、医生名称、医院、部门、详情链接

# 详细页
# 身高、体重、患病时长、过敏史
class Medical_database(Medical):
    __tablename__ = "medical_detail"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Disease_type = Column(String(200), nullable=False)
    Patient_Gender = Column(String(200), nullable=False)
    Patient_Age = Column(Integer(), nullable=False)
    Patient_Height = Column(Integer(), nullable=False)
    Patient_Weight = Column(Float(), nullable=False)
    Time_of_illness = Column(String(200), nullable=False)
    Allergy_history = Column(String(200), nullable=False)
    Consultation_time = Column(String(200), nullable=False)
    Description = Column(String(200), nullable=False)

    Doctor = Column(String(200), nullable=False)
    Hospital = Column(String(200), nullable=False)
    Department = Column(String(200), nullable=False)
    Detail_link = Column(String(200), nullable=False)