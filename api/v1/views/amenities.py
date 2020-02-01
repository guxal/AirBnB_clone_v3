#!/usr/bin/python3
"""show all amenities or only amenity id"""
from api.v1.views import app_views, index
from models.state import State
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, make_response, request


@app_views.route('/amenities', methods=['GET'])
def all_amenities():
    """list of all Amenities objects"""
    all_obj = []
    for obj in storage.all('Amenity').values():
        all_obj.append(obj.to_dict())
    return jsonify(all_obj)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def amenities_id(amenity_id):
    """the amenity based on the id"""
    obj = storage.get('Amenity', amenity_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenities_id(amenity_id):
    """delete to amenity for id"""
    obj = storage.get('Amenity', amenity_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    """Create new amenity"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    elif "name" not in data.keys():
        abort(400, "Missing Name")
    else:
        new_amenity = Amenity(**data)
        storage.new(new_amenity)
        storage.save()
    return make_response(jsonify(new_amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenities(amenity_id):
    """Update amenity for id"""
    data = storage.get('Amenity', amenity_id)
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
        return make_response(jsonify(data.to_dict()), 200)
