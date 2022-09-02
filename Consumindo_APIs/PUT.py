import json
import requests

URL = 'http://127.0.0.1:5000'

endpoint_login = URL + '/login'
body_login = {
    'login': 'Amanda',
    'senha': '123'
}
header_login = {
    'Content-Type': 'application/json'
}
resposta_login = requests.request('POST', endpoint_login, json=body_login, headers=header_login).json()
token = resposta_login['access_token']
print(token)

# PUT Hotel

endpoint_hotel_id = URL + '/hoteis/meuhotel'
body_hotel_id = {
    'nome': 'Meu Hotel Alterado',
    'estrelas': 4.3,
    'diaria': 290.45,
    'cidade': 'Guaratinguetá',
    'site_id': 3
}
header_hotel_id= {
    'Content-Type': 'application/json',
    "Authorization": "Bearer '{}'".format(token) 
}
resposta_hotel_id = requests.request('POST', endpoint_hotel_id, json=body_hotel_id, headers=header_hotel_id).json()

print(resposta_hotel_id)