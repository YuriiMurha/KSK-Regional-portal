from flask import Flask, Blueprint, render_template, request, jsonify
import json
import pandas as pd
import plotly.express as px
from arcgis.gis import GIS
from arcgis.mapping import WebMap
import requests
from waitress import serve

app = Flask(__name__)

    
# Load the report mapping from the JSON file
with open('reports.json') as f:
    report_mapping = json.load(f)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/get_report_id', methods=['POST'])
def get_report_id():
    data = request.get_json()
    selected_option = data.get('selectedOption')
    report_id = report_mapping.get(selected_option)

    if report_id:
        return jsonify({'report_id': report_id})
    else:
        return jsonify({'error': 'Report not found'}), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    file_name = file.filename
    if file_name == '':
        return 'No selected file'
    if file:
        # Get the report ID based on the file name
        report_id = report_mapping.get(file_name)

        if report_id:
            return jsonify({'report_id': report_id})
        else:
            return jsonify({'error': 'Report not found'}), 404


if __name__ == "__main__":
    # serve(app, host='0.0.0.0', port=8000)
    app.run(host='0.0.0.0', port=8000)
