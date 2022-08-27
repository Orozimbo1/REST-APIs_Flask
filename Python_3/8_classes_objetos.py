# Classe é um modelo ou uma representação de um objeto
# Objeto é uma instância de uma classe

class JogadorLoteria:
    def __init__(self, nome, numeros): 
        self.nome = nome
        self.numeros = numeros
    
    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria('Pedro', (12, 45, 67, 43, 55, 60))
jogador_2 = JogadorLoteria('Ana', (12, 33, 27, 53, 5, 60))
print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())
print(jogador_2.nome)
print(jogador_2.numeros)
print(jogador_2.total())