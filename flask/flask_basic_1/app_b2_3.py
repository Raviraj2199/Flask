from flask import *
app = Flask(__name__)

@app.route('/table/<int:num>')
def table(num):
    return render_template('message1.html',n=num)

if __name__=='__main':
    app.run(degug = False)