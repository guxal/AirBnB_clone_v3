#!/usr/bin/python3
from flask import Blueprint
app_views = Blueprint('app_views', __name__, '/api/v1')

from api.v1.views.index import *
