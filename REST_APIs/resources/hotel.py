from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
from resources.filtros import normalizando_caminho_parametros, consulta_sem_cidade, consulta_com_cidade
import sqlite3

caminho_parametro = reqparse.RequestParser()
caminho_parametro.add_argument('cidade', type=str)
caminho_parametro.add_argument('estrelas_min', type=float)
caminho_parametro.add_argument('estrelas_max', type=float)
caminho_parametro.add_argument('diaria_min', type=float)
caminho_parametro.add_argument('diaria_max', type=float)
caminho_parametro.add_argument('limit', type=int)
caminho_parametro.add_argument('offset', type=int)


class Hoteis(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = caminho_parametro.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalizando_caminho_parametros(**dados_validos)

        if not parametros.get('cidade'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_cidade, tupla)
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)

        hoteis = []
        for linha in resultado:
            hoteis.append({
            'hotel_id': linha[0],
            'nome': linha[1],
            'estrelas': linha[2],
            'diaria': linha[3],
            'cidade': linha[4],
            'site_id': linha[5]
            })

        return {'hoteis': hoteis} # SELECT * FROM hoteis


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The ield 'estrelas' cannot be left blank.")
    argumentos.add_argument('diaria', type=float, required=True, help="The field 'diaria' cannot be left blank.")
    argumentos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot be left blank.")
    argumentos.add_argument('site_id', type=int, required=True, help="Every hotel needs to be linked with a site.")

    def get(self, hotel_id):
        hotel = HotelModel.buscar_hotel(hotel_id)
        if hotel:
            return hotel.json(), 201
        return {'message': 'Hotel not found'}, 404

    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.buscar_hotel(hotel_id):
            return {"message": "Hotel '{}' already exists.".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel =  HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json(), 201

    @jwt_required()
    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        hotel_encontrado = HotelModel.buscar_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.atualizar_hotel(**dados)
            try:
                hotel_encontrado.save_hotel()
            except:
                return {'message': 'An internal error ocurred trying to save hotel.'}, 500
            return hotel_encontrado.json(), 200
        
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json(), 201

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.buscar_hotel(hotel_id)

        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500
            return {"message": "Hotel '{}' deleted.".format(hotel_id)}, 200

        return {'message': 'Hotel not found.'}, 404
