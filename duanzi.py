from flask import Flask, render_template, request
from userutils.Face_recongnition import Face
from userutils.Mysql_helper import Mysql_helper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/regist')
def regist():
    return render_template('regist.html')

@app.route('/login', methods=["POST"])
def login():
    requestData=request.form
    username=requestData['username']
    password=requestData['password']
    if Mysql_helper.check(username,password):
        sql = 'select * from daunzi'
        duanzilist=Mysql_helper.select(sql)
        return render_template('main.html', duanzilist=duanzilist)
    else:
        return "<h1>帐号或密码输入错误！</h1>"

@app.route('/faceLogin', methods=["POST"])
def faceLogin():
    result=Face.getImageResult()
    print(result)
    if result:
        sql = 'select * from daunzi'
        duanzilist = Mysql_helper.select(sql)
        return render_template('main.html', duanzilist=duanzilist)
    else:
        return "<h1>不是人脸或不是本人，请尝试用户名密码登陆！</h1>"

@app.route('/select', methods=["POST"])
def select():
    requestData = request.form
    searchword = requestData['searchword']
    sql = 'select * from daunzi where author like  \'%%%s%%\' or context like \'%%%s%%\''%(searchword,searchword)
    duanzilist = Mysql_helper.select(sql)
    return render_template('main.html', searchword=searchword, duanzilist=duanzilist)

@app.route('/registResult', methods=["POST"])
def registResult():
    requestData=request.form
    username = requestData['username']
    password = requestData['password']
    if Mysql_helper.check(username,password):
        return "<h1>帐号已存在！</h1>"
    else:
        sql="insert into user(username,password) values(\'%s\',\'%s\')"%(username,password)
        if Mysql_helper.update(sql)==0:
            return "<h1>注册失败，请查看使用说明</h1>"
        else:
            return "<h1>注册成功，请登录使用！</h1>"

if __name__ == '__main__':
    app.run()
