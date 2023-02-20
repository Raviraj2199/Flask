from flask import Flask

# flask constructor takes the name of 
# current module(__name__) as argument
 
app = Flask(__name__)

#route() decorator to tell Flask 
# what URL should trigger our function
#route() bind function to an URL
@app.route("/")

#defining the function 
def index():
    return 'This is Index Page'

@app.route('/home')
def home():
    return 'This is Home Page'

@app.route('/page2/<name>')
def hello_world2(name):
    return '<h1> %s you are awesome</h1>' %name

@app.route('/page3/<age>')
def hello_world3(age):
    return '<h1> your age is %s</h1>' %age


@app.route('/aboutus')
def aboutus():
    return '<h1>We are stratacent</h1>'

@app.route('/Contactus')
def Contactus():
    return '<h1>123456789</h1>'

@app.route('/Location')
def Location():
    return '<h1>1234.7899</h1>'


#main driver function 
if __name__ =="__main__":
    
    #run() method of class runs the application
    #on the local development server
    app.run(debug=False)