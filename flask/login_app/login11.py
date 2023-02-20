from flask import *
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/validate',methods =['POST','GET'])
def validate():
    if request.method == 'POST' and request.form["pass"] == "shweta":
       return redirect(url_for("success"))
    return redirect(url_for("login"))


@app.route('/success')
def success():
    return "<h1>Logged in successfully</h1>"

if __name__ == "__main__":
    app.run( debug = False)