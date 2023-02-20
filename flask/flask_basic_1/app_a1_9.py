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

if __name__ =="__main__":  
    app.run(debug = False) 
