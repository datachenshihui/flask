##  在开发之前，我们是用虚拟环境
####‘virtualenv --version’ 查看有没有虚拟环境的第三方工具
####‘virtualenv venv’ 创建虚拟环境
####‘source venv/Scripts/activate’ 激活虚拟环境
####‘deactivate’ 退出虚拟环境
##  虚拟环境下安装flask框架
####'pip install flask'  
##  git将代码提交
####1、将文件提交到缓存区'git add 文件名'
####2、将修改提交到本地仓库'git commit -m "提交说明描述"'
####3、关联到自己GitHub上的仓库 
#### 'git remote add origin https://github.com/用户名/仓库名.git'
#### https://github.com/datachenshihui/flask.git
####4、同步到远程仓库'git push -u origin master'  或者‘ git push’


##  对象（程序实例：Flask类的对象）
from flask import Flask,redirect,make_response,abort,render_template
from config import DevConfig
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(DevConfig)
bootstrap = Bootstrap(app)
##   app.route修饰器：就是“URL—>处理函数”的一个路由
####index()这样的函数就是一个视图函数，
####视图函数返回的响应可以使HTML的简单字符串，
####也可以是复杂的表视图函数返回的响应可以使HTML的简单字符串，也可以是复杂的表单

## 0  ##hello
@app.route('/')
def helloFunc():
	return '<h1>Hello World!!!</h1>'
## 1  ##返回response对象
####make_response函数可以接收1-3个参数
@app.route('/1')
def responseFunc():
	response = make_response('<h1> This document carries a cookies!</h1>')
	response.set_cookie('answer','42')	
	return response
## 2  ##尖括号部分是动态的
####还可以是 /user/<int:id> 就会匹配id为int型的url.
@app.route('/user/<name>')
def userFunc(name):
	return '<h1>Hello, %s.</h1>'%name
## 3  ##重定向
####redirect()函数
####调用自己的函数只要添加尾部即可
@app.route('/3')
def redirectFunc():
	return redirect('/52/小胖子')	
	##############？？？？？
## 4   ##错误处理
####abort()函数
@app.route('/4')
def abortFunc(id):
	return abort(404)
## 5   ##渲染模板，Jinja2
@app.route('/51')
def htmlFunc():
	return render_template('index.html')
####	name是user.html参数名
@app.route('/52/<names>')
def htmlnameFunc(names):
	return render_template('user.html',name = names)
##    启动服务器
if __name__ == '__main__':
	app.run()
