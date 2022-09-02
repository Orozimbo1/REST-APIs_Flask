from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank.")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank.")

class Usuario(Resource):
    #/usuarios/{usuario_id}

    def get(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)
        if usuario:
            return usuario.json()
        return {'message': 'User not found'}, 404

    @jwt_required()
    def delete(self, usuario_id):
        usuario = UsuarioModel.buscar_usuario(usuario_id)

        if usuario:
            try:
                usuario.delete_usuario()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500
            return {"message": "User '{}' deleted.".format(usuario_id)}, 200

        return {'message': 'User not found.'}, 404

class UsuarioCadastro(Resource):
    #/cadastro

    def post(self):
        dados = atributos.parse_args()

        if UsuarioModel.buscar_por_login(dados['login']):
            return {"message": "User '{}' already exists.".format(dados['login'])}, 404
        
        usuario = UsuarioModel(**dados)
        try:
            usuario.save_usuario()
        except:
            return {"message": "An internal error ocurred trying to save user."}, 500
        
        return {"message": "User created sucessfully!"}, 201
        
class UsuarioLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        usuario = UsuarioModel.buscar_por_login(dados['login'])

        if usuario and safe_str_cmp(usuario.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=usuario.usuario_id)
            return {"access_token": token_de_acesso}, 200
        return {"message": "The username or password is incorrect."}, 401 #Unauthorize

class UsuarioLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']# jwt token identifier
        BLACKLIST.add(jwt_id)
        return {"message": "Logged out successfully!"}, 200