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
    if request.method == 'POST':
        if request.form["pass"] == "shweta" and request.form["email"] == "shweta0318@gmail.com":
           return redirect(url_for("form"))
        elif request.form["pass"] == "gaurav" and request.form["email"] == "gaurav@gmail.com":
           return redirect(url_for("form"))
        elif request.form["pass"] == "ravi" and request.form["email"] == "ravi@gmail.com":
           return redirect(url_for("form"))
    return redirect(url_for("login"))



@app.route('/form')  
def form():  
   return render_template('form.html')  

@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      display = request.form  
      return render_template("display.html",display = display)  
if __name__ == "__main__":
    app.run( debug = False)