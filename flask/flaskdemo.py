from flask import Flask
from flask import render_template, request, redirect, url_for
from Point import *
app = Flask(__name__)

@app.route('/') # just run
def hello_world():
   return "aaa<h1>Hello World<h1><br><b>Hi</b>"

@app.route('/again') # http://127.0.0.1:5000/again
def again():
   return "again..."

def two():
   return "second"

@app.route('/hello/<name>') # http://127.0.0.1:5000/hello/itay
def hello_name(name):
   # p = Point(2, 3) # you can import other python files
   return 'Hello %s!' % name


@app.route('/blog/<int:postID>') # http://127.0.0.1:5000/blog/12 - one int parameter - into postID arg
def show_blog(postID):
   return 'Blog Number %d' % postID
@app.route('/rev/<float:revNo>') # http://127.0.0.1:5000/rev/1.5 - - one float parameter - into revNo arg
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/ynet')
def ynet():
   return redirect('https://www.ynet.co.il/home/0,7340,L-8,00.html')

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'
@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest
@app.route('/user/<name>')
def hello_user(name):
   # 1----
   #if name =='admin':
   #   return redirect('/admin')
   #else:
   #   return redirect(f'guest/{name}')
   # 2---- using url_for ( [method-name], args )
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/login',methods = ['POST', 'GET', 'PUT', 'DELETE']) # show 405
def login():
   if request.method == 'POST':
      return "post"
   elif request.method == 'PUT':
      return "put"
   elif request.method == 'GET':
      return "get"
   elif request.method == 'DELETE':
      return "delete"
   else:
      return "unknown"

@app.route('/hi') # make sure your have templates folder under THIS py file
def about():
   return render_template('hello.html')

@app.route('/hi_name/<user>')
def hello_your_name(user):
   return render_template('hello_name.html', name = user)

@app.route('/mark/<int:score>')
def marks(score):
   return render_template('show.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route("/withjs")
def index():
   return render_template("withjs.html")



############################## FORM
@app.route('/form1')
def form11():
   return render_template('form1.html') # change form1.html get/ post
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
@app.route('/log1',methods = ['POST', 'GET'])
def login2():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


############################## FORM - another example
@app.route('/student')
def student():
   return render_template('student.html')
@app.route('/result2',methods = ['POST', 'GET'])
def result2():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':

   app.add_url_rule('/two', 'two', two) # add route url - http://127.0.0.1:5000/two
   app.run()
   # app.run(port=7777)
   #app.run(debug=True) # to stop in break points