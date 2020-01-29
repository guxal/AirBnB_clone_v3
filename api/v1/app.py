#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)

host = environ.get('HBNB_API_HOST')
port = environ.get('HBNB_API_PORT')

app.register_blueprint(app_views)

app.register_blueprint(app_views)



@app.teardown_appcontext
def close(Error):
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
