from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return redirect(f'/result2/{name}/{age}')
    return render_template('home.html')
@app.route('/result2/<name>/<age>')


def result(name, age):
    return render_template('result2.html', name=name, age=age)


if __name__ =="__main__":
  app.run(debug=False)