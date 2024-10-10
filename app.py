from flask import Flask, render_template, jsonify
import json
from data_extract import extractData

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get event data
@app.route('/getEvent', methods=['GET'])
def get_event():
    event_data = extractData()  # Run your data extraction function
    return jsonify(event_data)  # Return the data as JSON

if __name__ == '__main__':
    app.run(debug=True)