from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3

def normalizando_caminho_parametros(cidade=None, estrelas_min=0, estrelas_max=5, diaria_min=0, diaria_max=10000, limit=50, offset=0, **dados):

    if cidade:
        return {
            'cidade': cidade,
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'limit': limit,
            'offset': offset
        }
    return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'limit': limit,
            'offset': offset
        }

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

        dados = caminho_parametro.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The ield 'estrelas' cannot be left blank.")
    argumentos.add_argument('diaria', type=float, required=True, help="The field 'diaria' cannot be left blank.")
    argumentos.add_argument('cidade', type=str, required=True, help="The field 'cidade' cannot be left blank.")

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
