from flask import Flask , render_template , redirect , url_for

app = Flask(__name__)   #creates flask app

@app.route("/")   #defines the hone route
def Hello():
    return "Hello"  

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/hello")

def hello_world():
    return  "Hello World"    


# Variables in Flask

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s!' % name


# Using url_for 
app.route('/user/<name>')
def hello_user():
    if name == 'admin' :
        return redirect(url_for('Hello_admin'))
    else:
        return redirect(url_for('Hello_guest', guest = name ))
    


# Using render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/useer')
def userrr():
    return render_template('insturc.html')










@app.route('/blog/<int:POSTID>')
def blog():
    return "Blog Number %d" % POSTID

@app.route('/revnum/<float:revid>')
def revnum():
    return "reverse id %f" % revid



