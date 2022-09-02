from email import header
import json
import requests

URL = 'http://127.0.0.1:5000'

# CADASTRO

endpoint_cadastro = URL + '/cadastro'
body_cadastro = {
    'login': 'Amanda',
    'senha': '123'
}
header_cadastro = {
    'Content-Type': 'application/json'
}
resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=header_cadastro).json()

print(resposta_cadastro)

# LOGIN

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

# POST Hotel

endpoint_hotel_id = URL + '/hoteis/meuhotel'
body_hotel_id = {
    'nome': 'Meu Hotel',
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

# POST Site

endpoint_site = URL + '/sites/www.meusite.com'

resposta_site = requests.request('POST', endpoint_site)

print(resposta_site.json())