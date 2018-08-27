from flask import Flask, send_from_directory
from flask_cache import Cache
import os

cache = Cache(config={'CACHE_TYPE': 'null'})

# Create Flask application
app = Flask(__name__, static_url_path='')

app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cache.init_app(app)

@app.route('/bower_components/<path:path>')
def send_bower(path):
    return send_from_directory(os.path.join(app.root_path, 'bower_components'), path)

@app.route('/dist/<path:path>')
def send_dist(path):
    return send_from_directory(os.path.join(app.root_path, 'dist'), path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.path.join(app.root_path, 'js'), path)

from app import views
