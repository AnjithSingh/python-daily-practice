from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello user! this is our fist flask app"

@app.route("/about")
def about():
    return "this is about us page"

@app.route("/contact")
def contact():
    return "this is our contact page"

@app.route("/submit" , methods = ["GET" , "POST"])
def submit():
    if request.method == "POST":
        return "You are sendind data"
    else:
        return "you are just viewing this form"