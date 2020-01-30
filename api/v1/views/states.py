#!/usr/bin/python3
"""show all states or only state id"""
from api.v1.views import app_views, index
from models.state import State
from models import storage
from flask import jsonify, abort, make_response, request


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def retrieve_obj():
    """list of all State objects"""
    all_obj = []
    for obj in storage.all('State').values():
        all_obj.append(obj.to_dict())
    return jsonify(all_obj)


@app_views.route('states/<state_id>', methods=['GET'], strict_slashes=False)
def retrieve_obj_id(state_id):
    """the state based on the id """
    obj = storage.get('State', state_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_id(state_id):
    """ funtion to deletes a State for id"""
    obj = storage.get('State', state_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'])
def create_state():
    """Create new state"""
    data = request.get_json(silent=True)
    if data is None:
        abort(404, "Not a JSON")
    elif "name" not in data.keys():
        abort(404, "Missing Name")
    else:
        new_state = State(**data)
        storage.new(new_state)
        storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id=None):
    """Update state for id"""
    data = storage.get('State', state_id)
    if data is None:
        abort(404)

    r = request.get_json(silent=True)
    if r is None:
        abort(404, "Not a JSON")
    else:
        for key, value in r.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(data, key, value)
        storage.save()
        return make_response(jsonify(data.to_dict()), 200)
