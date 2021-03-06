#!/usr/bin/python3
""" Flask Application """
from models import storage
from routes import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources=r'/api/*', allow_headers='*', origins='*', methods='*')

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)