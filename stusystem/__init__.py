from flask import Blueprint
# 创建蓝图，指定蓝图名称和模块名称
stu_sys = Blueprint("stu_sys",__name__,template_folder='templates')

from . import apps

