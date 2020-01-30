#!/usr/bin/python3
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.url_map.strict_slashes = False
host = environ.get('HBNB_API_HOST', '0.0.0.0')
port = environ.get('HBNB_API_PORT', '5000')

app.register_blueprint(app_views)


@app.teardown_appcontext
def close(Error):
    storage.close()


@app.errorhandler(404)
def errors_404(self):
    error = {'error': 'Not found'}
    return jsonify(error), 404


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
