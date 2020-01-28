#!/usr/bin/python3
from api.v1.views import app_views
import models
from models.city import City
import json

@app_views.route('/api/v1/status')
def json_status():
    var = '{\n  "status": "OK"\n}\n'
    return var

@app_views.route('/api/v1/stats')
def endpoint_stats():
    amenities =  '{\n  "amenities": '+str(models.storage.count("Amenity"))+','
    cities = '\n  "cities": '+str(models.storage.count("City"))+',' 
    places = '\n  "places": '+str(models.storage.count("Place"))+','
    reviews = '\n  "reviews": '+str(models.storage.count("Review"))+','
    states = '\n  "states": '+str(models.storage.count("State"))+','
    users = '\n  "users": '+str(models.storage.count("User"))+'\n}\n'
    return amenities + cities + places + reviews + states + users