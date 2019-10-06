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
