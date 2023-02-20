from flask import *
app = Flask(__name__)


@app.route('/')  
def empform():  
   return render_template('employee.html')  


@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      display = request.form  
      return render_template("display.html",display = display)  

if __name__ == "__main__":
    app.run( debug = False)