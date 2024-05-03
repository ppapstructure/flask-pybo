import os

# BASE_DIR = C:\projects\myproject 경로 가져옴
BASE_DIR = os.path.dirname(__file__)
# print('CMD 경로 :',BASE_DIR)

# SQLALCHEMY에게 데이터베이스 파일의 경로가 어디 있는지 알려줌
# SQLALCHEMY_DATABASE_URI = sqlite:///C:\projects\myproject\pybo.db
# sqlite 대신 사용 가능 SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@host/database_name'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# os.path.join(BASE_DIR, 'pybo.db') : 데이터 베이스 파일의 전체경로
# print(SQLALCHEMY_DATABASE_URI)

# 객체 변경사항 추적x (이걸 안해야 성능이 향상됨)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"