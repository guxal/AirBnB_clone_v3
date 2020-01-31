#!/usr/bin/python3
"""show all cities or only city id"""
from api.v1.views import app_views, index
from models.state import State
from models import storage
from models.city import City
from flask import jsonify, abort, make_response, request


@app_views.route('/cities/', methods=['GET'], strict_slashes=False)
def all_cities():
    """list of all City objects"""
    all_obj = []
    for obj in storage.all('City').values():
        all_obj.append(obj.to_dict())
    return jsonify(all_obj)


@app_views.route('states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def state_city_id(state_id):
    """the state based on the id """
    obj = storage.get('State', state_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('cities/<city_id>', methods=['GET'], strict_slashes=False)
def city_id(city_id):
    """the city based on the id """
    obj = storage.get('City', city_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_id(state_id):
    """ funtion to deletes a City for id"""
    obj = storage.get('City', city_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create new city"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    elif "name" not in data.keys():
        abort(400, "Missing Name")
    else:
        new_city = City(**data)
        storage.new(new_city)
        storage.save()
    return make_response(jsonify(new_amenity.to_dict()), 201)


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
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(data, key, value)
        storage.save()
        storage.reload()
        return make_response(jsonify(data.to_dict()), 200)
