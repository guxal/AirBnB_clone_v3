#!/usr/bin/python3
"""show all states or only state id"""
from api.v1.views import app_views, index
from models import storage, state
from flask import jsonify, abort


@app_views.route('/states/', methods=['GET'])
def retrieve_obj():
    all_obj = []
    for obj in storage.all('State').values():
        all_obj.append(obj.to_dict())
    return jsonify(all_obj)


@app_views.route('states/<state_id>', methods=['GET'])
def retrieve_obj_id(state_id):
    obj = storage.get('State', state_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())
