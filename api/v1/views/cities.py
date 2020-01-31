#!/usr/bin/python3
"""show all cities or only city id"""
from api.v1.views import app_views, index
from models.state import State
from models import storage
from models.city import City
from flask import jsonify, abort, make_response, request


@app_views.route('states/<state_id>/cities', methods=['GET'])
def state_city_id(state_id):
    """ the state based on the id """
    data = storage.get('State', state_id)
    if data is None:
        abort(404)
    cities = [city.to_dict() for city in data.cities]
    return jsonify(cities), 200


@app_views.route('cities/<city_id>', methods=['GET'])
def city_id(city_id):
    """ the city based on the id """
    data = storage.get('City', city_id)
    if data is None:
        abort(404)
    return jsonify(data.to_dict())


@app_views.route('cities/<city_id>', methods=['DELETE'])
def delete_city_id(city_id):
    """ funtion to deletes a City for id"""
    data = storage.get('City', city_id)
    if data is None:
        abort(404)
    else:
        storage.delete(data)
        storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create new city"""
    data = storage.get('State', state_id)
    r = request.get_json(silent=True)
    if r is None:
        abort(400, "Not a JSON")
    elif "name" not in r.keys():
        abort(400, "Missing Name")
    else:
        r['state_id'] = state.id
        new_city = City(**r)
        storage.new(new_city)
        storage.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update city for id"""
    data = storage.get('City', city_id)
    if data is None:
        abort(404)

    r = request.get_json(silent=True)
    if r is None:
        abort(400, "Not a JSON")
    else:
        for key, value in r.items():
            if key in ['id', 'created_at', 'updated_at', 'state_id']:
                pass
            else:
                setattr(data, key, value)
        storage.save()
        return make_response(jsonify(data.to_dict()), 200)
