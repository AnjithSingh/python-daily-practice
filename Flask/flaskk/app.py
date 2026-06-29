from flask import Flask , request , redirect , url_for , Response

app = Flask(__name__)

app.secret_key = "ksjdhakhdbakbhd"

@app.route("/" , methods = ["GET" , "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == 'admin' and password == '1234':
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Credentails, Try again" , mimetype = 'text/plain')
    
    else:
        return '''
                <h2>Login Page</h2>
                <form method = "POST>
                Username : <input type = "text" name = "username" ><br>
                Password : <input type = "text" name = "password"><br> 
                <input type = "submit" value = "login">
                </form>
               '''
        
# welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome! ,{session["user"]}! </h2>
        <a href = {url_for("logout")}>Logout</a>

'''
    return redirect(url_for('login'))



#logut route

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))




