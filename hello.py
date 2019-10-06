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
####4、同步到远程仓库'git push -u origin master'


##  对象（程序实例：Flask类的对象）
from flask import Flask
app = Flask(__name__)
 
##   app.route修饰器：就是“URL—>处理函数”的一个路由
####index()这样的函数就是一个视图函数，
####视图函数返回的响应可以使HTML的简单字符串，
####也可以是复杂的表视图函数返回的响应可以使HTML的简单字符串，也可以是复杂的表单
@app.route('/')
def index():
	return '<h1>Hello World!!!</h1>'
####尖括号部分是动态的
####还可以是 /user/<int:id> 就会匹配id为int型的url.
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s.</h1>'%name
	
##    启动服务器
if __name__ == '__main__':
	app.run(debug=True)
