meu_dicionário = {'nome': 'Joao', 'idade': '30'}
print(meu_dicionário['nome'])# Joao
print(meu_dicionário['idade'])# 30

lista_dicionario = [
    {'nome': 'Joao', 'idade': '30'},
    {'nome': 'Gabriela', 'idade': '25'},
    {'nome': 'Julia', 'idade': '32'},
    {'nome': 'Leandro', 'idade': '45'}
]
print(lista_dicionario[1]['nome'])# Gabriela
lista_dicionario[1]['idade'] = 18 # Alterando o valor "idade"
print(lista_dicionario[1]['idade']) # 18