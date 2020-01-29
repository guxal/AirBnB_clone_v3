#!/usr/bin/python3
"""start your API"""
from api.v1.views import app_views
import models
from models.city import City
from flask import jsonify
import json


@app_views.route('/status')
def json_status():
    """will be to return the status"""
    var = {"status": "OK"}
    return jsonify(var)


@app_views.route('/stats')
def endpoint_stats():
    """retrieves the number of each objects by type"""
    new_obj = {"amenities": models.storage.count("Amenity"),
               "cities": models.storage.count("City"),
               "places": models.storage.count("Place"),
               "reviews": models.storage.count("Review"),
               "states": models.storage.count("State"),
               "users": models.storage.count("User")
               }
    return jsonify(new_obj)
