#!/usr/bin/python3
"""show all users or only user id"""
from api.v1.views import app_views, index
from models.state import State
from models import storage
from models.amenity import Amenity
from models.user import User
from flask import jsonify, abort, make_response, request


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def all_users():
    """list of all users objects"""
    all_obj = []
    for obj in storage.all('User').values():
        all_obj.append(obj.to_dict())
    return jsonify(all_obj)


@app_views.route('users/<user_id>',
                 methods=['GET'], strict_slashes=False)
def user_id(user_id):
    """the user based on the id """
    obj = storage.get('User', user_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user_id(user_id):
    """ funtion Delete a user for id"""
    obj = storage.get('User', user_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/user', methods=['POST'])
def create_user():
    """Create new user"""
    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")
    elif "name" not in data.keys():
        abort(400, "Missing Name")
    else:
        new_user = User(**data)
        storage.new(new_user)
        storage.save()
        storage.reload()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id=None):
    """Update user for id"""
    data = storage.get('User', user_id)
    if data is None:
        abort(404)

    r = request.get_json(silent=True)
    if r is None:
        abort(400, "Not a JSON")
    else:
        for key, value in r.items():
            if key in ['id', 'created_at', 'updated_at', 'email']:
                pass
            else:
                setattr(data, key, value)
        storage.save()
        return make_response(jsonify(data.to_dict()), 200)
