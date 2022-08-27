# Listas
# Jeito mais trabalhoso e menos eficaz de gerar média
nota_1 = 5
nota_2 = 2
nota_3 = 9
nota_4 = 6
nota_5 = 8

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5)/5
print(media)

# Jeito menos trabalhoso e mais eficaz de gerar média 
notas = [5, 2, 9, 6, 8]

notas.append(7)# Adiciona um valor à uma lista
print(notas[0]) # 5 Acessando o primeiro elemento da lista
print(notas[-1]) # 7 Acessando o último elemento da lista

media = sum(notas)/len(notas)
print(media)

# Tuplas
tupla = (1, 2, 3) # São unicas e não podem ser modificadas a menos que se crie outra
print(tupla)
tupla += (2,) # Esta sendo criada outra tupla com os mesmos valores da anterior acrescentando o "2" ao final
print(tupla)

#Sets
set_nota = {1, 2, 3, 4, 4, 5, 5} # Podem ter valores repetidos mas não serão lidos, e não possuem índices
print(set_nota) # {1, 2, 3, 4, 5} # Mesmo que tenha dois valores com os números "4" e "5" será lido uma única vez
set_nota.add(7) # Adiciona um valor, nesse caso o número "7"
print(set_nota) # {1, 2, 3, 4, 5, 7}
