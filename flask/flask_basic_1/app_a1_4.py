from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index(): 
    if request.method == "POST":  
        option  = request.form.get('option')
        num1  = request.form.get('num1')
        num2  = request.form.get('num2')

        if option == "Addition":
            data = num1 + num2
        elif option == "subtraction":
            datd = num1 - num2
        elif option == "division":
            datd = num1 / num2
        elif option == "multiplication":
            data = num1 * num2
        return render_template('result.html', data=data)
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=False)