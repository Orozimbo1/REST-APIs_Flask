saudacao = "Ola Mundo"

for letra in saudacao:
    print(letra)

lista_numeros = list(range(11))# Cria uma lista automática de início "0" at´´e "10"
print(lista_numeros)# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla_numeros = tuple(range(11))# Cria uma tupla automática de início "0" at´´e "10"
print(tupla_numeros)# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
set_numeros = set(range(11))# Cria um set automática de início "0" at´´e "10"
print(set_numeros)# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = list(range(0,11,2))
print(numeros_pares)
numeros_impares = list(range(1,10,2))
print(numeros_impares)

for numero in numeros_pares:
    print(numero ** 2)

x = 0
while x <= 10 :
    print(x ** 2)
    x += 2