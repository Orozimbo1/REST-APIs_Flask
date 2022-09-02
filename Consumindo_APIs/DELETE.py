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

# Delete hotel

endpoint_hotel_id = URL + '/hoteis/meuhotel'
header_hotel_id= {
    'Content-Type': 'application/json',
    "Authorization": "Bearer '{}'".format(token) 
}
resposta_delete = requests.request('DELETE', endpoint_hotel_id, headers=header_hotel_id).json()

print(resposta_delete)

# Delete usuario

endpoint_usuario_id = URL + '/usuarios/1'
header_usuario_id= {
    'Content-Type': 'application/json',
    "Authorization": "Bearer '{}'".format(token) 
}
resposta_delete = requests.request('DELETE', endpoint_usuario_id, headers=header_usuario_id).json()

print(resposta_delete)

# Delete site

endpoint_site = URL + '/sites/www.meusite.com'
header_site = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer '{}'".format(token) 
}
resposta_delete = requests.request('DELETE', endpoint_site, headers=header_site).json()

print(resposta_delete)
