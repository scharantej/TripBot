
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit_plan', methods=['POST'])
def submit_plan():
    destination = request.form['destination']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    activities = request.form['activities']

    # Validate input
    if not destination or not start_date or not end_date or not activities:
        flash('Please fill out all fields.')
        return redirect(url_for('index'))

    # Save plan to database

    # Redirect to success page
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
