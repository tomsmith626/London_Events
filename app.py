from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the main page with the button
@app.route('/')
def index():
    return render_template('index.html')

# Route triggered when button is clicked
@app.route('/findEvent', methods=['POST'])
def findEvent():
    # Run your Python script here
    subprocess.run(['python3', 'data_extract.py'])
    return redirect(url_for('index'))  # Redirect back to the main page after running the script

if __name__ == '__main__':
    app.run(debug=True)