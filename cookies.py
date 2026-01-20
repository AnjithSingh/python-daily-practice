import flask from Flask , url_for, render_template, request , make_response 

app = Flask(__name__)
@app.route("/")

def index():
    return render_template('index.html')


@app.route('/setcookies',methods = ['GET' , 'POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('cookie.html'))
        resp.set_cookie('UserID',user)
        return resp
    

@app.route('/getcookie')
def getcookie():
    name = request.cookie.get('UserID')
    return '<h1>Welcome '+name+' <h1>'

if __name__ == "__main__":
    app.run()
