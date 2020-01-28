#!/usr/bin/python3
from api.v1.views import app_views
import models
from models.city import City
from flask import jsonify
import json

@app_views.route('/api/v1/status')
def json_status():
    var = {"status": "OK"}
    return jsonify(var)

@app_views.route('/api/v1/stats')
def endpoint_stats():
    new_obj = {"amenities" : models.storage.count("Amenity"),
                "cities" : models.storage.count("City"),
                "places": models.storage.count("Place"),
                "reviews": models.storage.count("Review"),
                "states": models.storage.count("State"),
                "users": models.storage.count("User")
    }
    return jsonify(new_obj)

@app_views.route('/api/v1/nop')
def errors_404():
    error = {'error': 'Not found'}
    return jsonify(error)