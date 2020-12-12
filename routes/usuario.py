#!/usr/bin/python3
""" TODO lo de usuarios """
from models.animal import Animal
from models.usuario import Usuario
from models import storage
from routes import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/usuario/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Login
    """
    data = request.get_json(force=True)
    users = storage.all(Usuario)
    for key, value in users.items():
        data_user = value.to_dict()
        if data_user.get('correo') == data.get('correo') and data_user.get('contraseña') == data.get('contraseña'):
            return jsonify({'status': 'ok', 'data': data_user})
    return make_response(jsonify({'error': 'usuario/contraseña incorrectos'}), 400)

@app_views.route('/usuario/', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Trae todos los usuarios
    """
    users = storage.all(Usuario)
    list_users = []
    
    for user in users.values():
        list_users.append(user.to_dict())
    return jsonify(list_users)

@app_views.route('/usuario/<usuario_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(usuario_id):
    """
    Elimina un usuario con el id
    """
    user = storage.get(Usuario, int(usuario_id))
    if not user:
        abort(404, description="Not a JSON")
    
    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/usuario/', methods=['POST'], strict_slashes=False)
def create_user():
    data = request.get_json(force=True)
    if not data:
        abort(400)
    instance = Usuario(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/usuario/<usuario_id>', methods=['PUT'], strict_slashes=False)
def update_user(usuario_id):
    usuario = storage.get(Usuario, int(usuario_id))
    if not usuario:
        abort(400)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    
    ignore = ['id']

    for key, value in data.items():
        if key not in ignore:
            setattr(usuario, key, value)
    storage.save()
    return make_response(jsonify(usuario.to_dict()), 200)
