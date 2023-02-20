#rendering template
#In flask, html file are served from the 'templates' folder by default and all the static file; 
# images, css, js, etc are served from the 'static' folder
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('app_a1_5_message2.html')

@app.route("/deals")
def deals():
    return render_template('dealspage.html')

@app.route("/error")
def error():
    return render_template('errorpage.html')

@app.route("/front")
def front():
    return render_template('frontpage.html')


if __name__=="__main__":
    app.run(debug=False)
    
