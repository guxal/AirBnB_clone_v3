#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import *
import api.v1.views.states


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
