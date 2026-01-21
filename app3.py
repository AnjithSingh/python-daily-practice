from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, Welcome to Viralhit"
  
@app.route("/")
def index():
    return "Homepage of Viralhit"

if __name__ == "__main__":
    app.run(debug=True)