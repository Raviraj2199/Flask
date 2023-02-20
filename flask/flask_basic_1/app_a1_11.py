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


#@app.route('/Ceo_LoggedIn')  
def Ceo_LoggedIn():  
    return '<h1>Welcome you are logged in as CEO</h1>'  
app.add_url_rule("/Ceo_LoggedIn","Ceo_LoggedIn",Ceo_LoggedIn) 

#@app.route('/Employee_LoggedIn')  
def Employee_LoggedIn():  
    return '<h2>Welcome to your Customer relationship Management</h2>'  
app.add_url_rule("/Employee_LoggedIn","Employee_LoggedIn",Employee_LoggedIn) 

#@app.route('/Clients_LoggedIn')  
def Clients_LoggedIn():  
    return '<h1>Welcome to Stratacent</h1>'  
app.add_url_rule("/Clients_LoggedIn","Clients_LoggedIn",Clients_LoggedIn) 



# so this is where the url_function helps in redirects (dynamic redirect)  
@app.route('/login/<role>')  
def user(role):  
    if role == 'Ceo_LoggedIn':  
        return redirect(url_for('Ceo_LoggedIn'))  
    if role == 'Employee_LoggedIn':  
        return redirect(url_for('Employee_LoggedIn'))  
    if role == 'Clients_LoggedIn':  
        return redirect(url_for('Clients_LoggedIn')) 

if __name__ =="__main__":  
    app.run(debug = False) 
