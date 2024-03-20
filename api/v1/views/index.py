#!/usr/bin/python3
"""
import app_views,
create a route /status on the object
app_views that returns a JSON

"""

from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review

classes_dictionary = {"amenities": Amenity, "cities": City,
    "places": Place, "reviews": Review, "states": State, "users": User}

@app_views.route('/status')
def status():
    """return status: OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """returns count of models"""
    classes = {}
    for obj in classes_dictionary:
        classes.update({obj: storage.count(classes_dictionary[obj])})
    return jsonify(classes)
