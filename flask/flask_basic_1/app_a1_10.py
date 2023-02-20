"""
Project 7 
The add_url_rule() function
There is one more approach to perform routing for the flask web application that can be done by using the add_url() function of the 
Flask class. The syntax to use this function is given below.

add_url_rule(<url rule>, <endpoint>, <view function>)  
This function is mainly used in the case if the view function is not given and we need to connect a view function to an endpoint 
externally by using this function.
"""


from flask import *   
app = Flask(__name__)

#@app.route('/about') 
def about():  
    return "This is about page"  
app.add_url_rule("/about","about1",about) 


#@app.route('/about/<text>') 
def about2(text):  
    return "This is about page %s " %text
app.add_url_rule("/about/<text>","about2",about2) 


#@app.route('/admin')  
def admin():  
    return 'you logged in as admin'  
app.add_url_rule("/admin","admin1",admin) 

#@app.route('/librarion')  
def librarion():  
    return 'you logged in as librarion'  
app.add_url_rule("/librarion","librarion",librarion) 

#@app.route('/student')  
def student():  
    return 'you logged in as student'  
app.add_url_rule("/student","student",student) 



# so this is where the url_function helps in redirects (dynamic redirect)  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student')) 

if __name__ =="__main__":  
    app.run(debug = False) 


"""
Benefits of the Dynamic URL Building
1)It avoids hard coding of the URLs.
2)We can change the URLs dynamically instead of remembering the manually changed hard-coded URLs.
3)URL building handles the escaping of special characters and Unicode data transparently.
4)The generated paths are always absolute, avoiding unexpected behavior 
of relative paths in browsers.
5)If your application is placed outside the URL root, for example, in /myapplication 
instead of /, url_for() properly handles that for you.

"""