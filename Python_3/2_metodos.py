def meu_metodo():
    print('Olá mundo!!')
meu_metodo() # Olá mundo!!

def soma_dois_valores(x, y):
    soma = x + y
    return soma
soma = soma_dois_valores(10.5, 5) #15.5
print(soma) # Reprodução do código no terminal
print(int(soma)) #15 Tranforma número flutuante para número inteiro
print(float(soma)) # Tranforma número inteiro para número flutuante
print(len('Olá')) # 3 Mostrará o tamanho do elemento, nesse caso "Olá"
x = -10
print(abs(x)) # 10 Mostra o valor absoluto
lista = [1, 2, 3, 4]
print(sum(lista)) # 10 Retorna a soma de uma lista
print(min(lista)) # 1 Retorna o valor mínimo de uma lista
print(max(lista)) # 4 Retorna o valor máximo de uma lista
print(round(10.9)) # 11 Arredonda o valor
print(round(10.943564, 2)) # 10.94 Arredonda o valor para o numero de casas que for definido, nesse caso "2"