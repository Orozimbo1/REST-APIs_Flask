from ast import arguments
from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

class Usuario(Resource):

    def get(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            return usuario.json(), 201
        return {'message': 'User not found'}, 404

    def delete(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)

        if usuario:
            try:
                usuario.delete_usuario()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500
            return {"message": "User '{}' deleted.".format(usuario_id)}, 200

        return {'message': 'User not found.'}, 404