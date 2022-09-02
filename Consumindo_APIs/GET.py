import json
import requests

URL = 'http://127.0.0.1:5000'

# GET hoteis

resposta_hoteis = requests.request('GET', URL + '/hoteis')

print(resposta_hoteis.status_code)

hoteis = resposta_hoteis.json()
lista_hoteis = hoteis['hoteis']
for hotel in lista_hoteis:
    print(hotel['nome'])

# GET hoteis por id

resposta_hotel_por_id = requests.request('GET', URL + '/hoteis/meuhotel')

print(resposta_hotel_por_id.json())

# GET usuarios por id

resposta_usuarios_por_id = requests.request('GET', URL + '/usuarios/1')

print(resposta_usuarios_por_id.json())

# GET sites

resposta_sites = requests.request('GET', URL + '/sites')

print(resposta_sites.json())

# GET usuarios por url

resposta_usuarios_por_url = requests.request('GET', URL + '/sites/www.meusite.com')

print(resposta_usuarios_por_url.json())