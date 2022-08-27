lista = [x for x in range(5)]
print(lista)

numeros_pares = [x for x in range(11) if x % 2 == 0]
print(numeros_pares)

numeros_impares = [x for x in range(10) if x % 2 == 1]
print(numeros_impares)

pessoas = [" Ana", "FELIpe", " JoAo ", "AmAnDa "]
for pessoa in pessoas:
    print(pessoa.strip())# retira o espaço
    print(pessoa.capitalize())# Primeira letra maiúscula e o resto minúscula
    print(pessoa.upper())# Todas letras maiúsculas
    print(pessoa.lower())# Todas as letras minúsculas

pessoas_formatadas = [pessoa.strip().capitalize() for pessoa in pessoas]
print(pessoas_formatadas)