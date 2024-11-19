
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    if request.method == 'POST':
        try:
            # Get form data
            grade1 = float(request.form['grade1'])
            grade2 = float(request.form['grade2'])
            grade3 = float(request.form['grade3'])
            attendance = float(request.form['attendance'])
            
            # Calculate average and determine pass/fail
            average = (grade1 + grade2 + grade3) / 3
            status = 'Aprobado' if average >= 40 and attendance >= 75 else 'Reprobado'
            
            return render_template('exercise1.html', average=average, status=status)
        except ValueError:
            return render_template('exercise1.html', error="Please enter valid numbers.")
    return render_template('exercise1.html')

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    if request.method == 'POST':
        # Get names from form
        names = [request.form['name1'], request.form['name2'], request.form['name3']]
        # Determine the longest name
        longest_name = max(names, key=len)
        name_length = len(longest_name)
        return render_template('exercise2.html', longest_name=longest_name, name_length=name_length)
    return render_template('exercise2.html')

if __name__ == '__main__':
    app.run(debug=True)
