from flask import Flask, render_template, url_for, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
        if request.method == 'POST':
            num1 = request.form['num1']
            num2 = request.form['num2']
            operation = request.form['operation']
            note=""

        try:
            if operation == 'add':
                result = float(num1) + float(num2)
                return render_template('simple.html', result=result, num1=num1, num2=num2, operation=operation)
            elif operation == 'subtract':
                result = float(num1) - float(num2)
                return render_template('simple.html', result=result, num1=num1, num2=num2, operation=operation)
            elif operation == 'multiply':
                result = float(num1) * float(num2)
                return render_template('simple.html', result=result, num1=num1, num2=num2, operation=operation)
            elif operation == 'divide':
                result = float(num1) / float(num2)
                return render_template('simple.html', result=result, num1=num1, num2=num2, operation=operation)
        except ValueError:
            return render_template('simple.html',result=0, note="Math Error !!")
        except ZeroDivisionError:
            return render_template('simple.html',result=0, note="Math Error !!")
        
@app.route('/calculate_advanced', methods=['POST'])
def calculate_advanced():
    if request.method == 'POST':
        num1 = request.form['num1']
        operation = request.form['operation']
        note=""

        try:
            if operation == 'sin':
                result = math.sin(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            elif operation == 'cos':
                result = math.cos(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            elif operation == 'tan':
                result = math.tan(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            elif operation == 'sqrt':
                result = math.sqrt(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            elif operation == 'log':
                result = math.sqrt(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            elif operation == 'exp':
                result = math.exp(float(num1))
                return render_template('advanced.html', result=result, num1=num1, operation=operation)
            
        except ValueError:
            return render_template('advanced.html',result=0, note="Math Error !!", color = "alert-danger")


@app.route('/simple')
def simple():
    return render_template('simple.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)