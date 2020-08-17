from flask import render_template,request,redirect
from manage import Stu,db
from . import stu_sys
from sqlalchemy import or_

# 主页
@stu_sys.route('/index')
def index():
    students = Stu.query.all()
    for a in students:
        print(a.id)
    return render_template("index.html",students=students)

# 添加学生信息
@stu_sys.route('/add_stu',methods=['GET','POST'])
def addstu():
    if request.method == "GET":
        return render_template("add.html")
    else:
        name = request.form.get("name")
        sex = request.form.get("sex")
        age = request.form.get("age")
        grade = request.form.get("grade")
        major = request.form.get("major")
        stu_id = request.form.get("stu_id")
        score = request.form.get("score")
        stu = Stu(name=name, sex=sex, age=int(age),grade=grade,major=major,stu_id=stu_id,score=int(score))
        db.session.add(stu)
        db.session.commit()
        return redirect("index")

# 查找学生信息
@stu_sys.route('/find_stu',methods=['GET'])
def findstu():
    # 获取搜索框的值
    str = request.args.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = Stu.query.filter(or_(Stu.stu_id == str,Stu.name ==str))
    return render_template("show.html", students=students)

# 删除学生信息
@stu_sys.route('/del_stu',methods=['GET'])
def deletestu():
    # 获取需要删除的学生对象的id
    del_id = request.args.get('del_id')
    # 先查找单个对象，然后进行删除
    stu = Stu.query.get(del_id)
    db.session.delete(stu)
    db.session.commit()
    # 删除之后，重定向到首页
    return redirect("index")

# 修改学生信息
@stu_sys.route('/up_stu',methods=['GET','POST'])
def updatestu():
    # 根据表单提交的方式判断是查询单个还是修改之后提交数据库
    if request.method == "GET":
        # 获取要修改的对象的sid查询单个的学生
        up_id = request.args.get('update_id')
        #  根据学生的sid查询单个学生进行修改
        student = Stu.query.get(up_id)
        # 跳转到修改页面，并携带修改对象的信息
        return render_template("update.html",student=student)
    # 表单提交，进行修改学生
    else:
        # 获取需要修改的学生对象的信息
        update_id=request.form.get("id")
        update_student = Stu.query.get(update_id)
        update_name=request.form.get("name")
        update_sex=request.form.get("sex")
        update_age=request.form.get("age")
        update_grade = request.form.get("grade")
        update_major = request.form.get("major")
        update_stu_id = request.form.get("stu_id")
        update_score = request.form.get("score")
        print('update_stu_id=',update_stu_id)
        # 修改对象的信息
        update_student.name=update_name
        update_student.sex=update_sex
        update_student.age=update_age
        update_student.grade = update_grade
        update_student.major = update_major
        update_student.stu_id = update_stu_id
        update_student.score = update_score
        # 保存对象到数据库
        db.session.commit()
        # 重定向到首页，显示学生信息
        return redirect("index")

# 排序
@stu_sys.route('/sort_stu')
def sortstu():
    pass

# 统计学生人数
@stu_sys.route('/count_stu')
def countstu():
    pass






