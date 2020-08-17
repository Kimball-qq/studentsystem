from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from stusystem import stu_sys


app = Flask(__name__)

class Config:
    DEBUG = True
    SECRET_KEY = "mabo"
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/studentsystem"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config.from_object(Config)
# 数据库
db = SQLAlchemy(app)


app.register_blueprint(stu_sys,url_prefix="/stusys")
manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)

class Stu(db.Model):
    __tablename__ = 'stu_system'
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(64), nullable=False)  # 姓名
    age = db.Column(db.Integer,default='20')
    sex = db.Column(db.String(10), default='男')  # 性别
    major = db.Column(db.String(512), nullable=False)  # 专业
    grade = db.Column(db.String(64), default=1)  # 年级
    stu_id = db.Column(db.String(64), default=0)  # 学号
    score = db.Column(db.Integer, default=0)  # 成绩


if __name__ == "__main__":
    print(app.url_map)
    manager.run()