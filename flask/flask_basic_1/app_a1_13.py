from flask import *

app = Flask(__name__)


@app.route('/home/<int:age>')
def home(age):
    return "Äge = %d" %age

@app.route('/home/<text>/<int:age>')
def home1(text,age):
    return f"Name={text} ,Äge = {age}"

#Get client with id between 9000 to 9999 as valid clients

@app.route('/CEO')  
def CEO():
    return("Welcome CEO")

@app.route('/Clients')  
def Clients():
    return("Welcome Clients")

    
def Employees_loggedin():
    return("<h1>Welcome to CRM</h1>")
app.add_url_rule("/Employees_loggedin","Employeeslogin",Employees_loggedin)


def Clients_loggedin():
       return"<h1>Welcome to Stratacent</h1>"
app.add_url_rule("/Clients_loggedin","Clients_loggedin",Clients_loggedin)


@app.route("/login/<role>/<int:id>")
def login(role,id):
    if role == "Clients" and id in range(9000,9999):
      return redirect(url_for('Clients_loggedin'))
    elif role == "Clients" and id not in range(9000,9999):
      return "ïnvalid client"

  

@app.route("/login/<role>/<id>")
def login1(role,id):
    if role == "Clients":
      return "Welcome to Stratacent Yo you are not client with valid id"   

if __name__ == "__main__":
    app.run( debug = False)