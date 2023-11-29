from flask import Flask, render_template, jsonify, send_from_directory
from flasgger import Swagger, swag_from
from api.kismet_api import KismetAPI
import json
import random
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for development
kismet_api = KismetAPI()

swagger = Swagger(app)
app.config['SWAGGER'] = {
    'title': 'Kismet Fortune Telling API',
    'uiversion': 3,
    'hide_top_bar': True,
    'specs_route': '/api/swagger/',
}


@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())  # Adjust this path if needed
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fortune', methods=['POST'])
@swag_from('kismet.yml')
def fortune():
    fortune_result = kismet_api.get_random_fortune()
    return jsonify({'fortune': fortune_result})

if __name__ == '__main__':
    app.run(debug=True)

