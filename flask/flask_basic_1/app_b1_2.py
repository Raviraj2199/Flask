from flask import *  
app = Flask(__name__)  

def success_func(name):
    return "welcome %s" %name

app.add_url_rule("/success/<name>","success",success_func)

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    return render_template('login.html')



if __name__ == '__main__':
   app.run(debug = False) 