#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.animal import Animal
from models import storage
from routes import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/animal/<animal_id>/', methods=['POST'], strict_slashes=False)
def deee(animal_id): 
    """
    Get animal where id
    """
    animal = storage.get(Animal, int(animal_id))
    if not animal:
        abort(400)
    print(animal.to_dict())
    return jsonify(animal.to_dict())