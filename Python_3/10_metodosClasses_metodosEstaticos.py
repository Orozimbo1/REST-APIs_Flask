import datetime
minha_data = datetime.date(2019, 4, 11)
print(minha_data)

class Funcionario:
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    
    @classmethod # Métodos de classe
    def deinir_novo_aumento(cls, novo_aumento): # Não é usado mais o "self", e sim o "cls"
        cls.aumento = novo_aumento
    
    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


fabio = Funcionario('Fabio', 4000)
print(fabio.dados()) # 'Fabio', '4000'

fabio.aplicar_aumento() # Aumento de 4%
print(fabio.dados()) # 'Fabio', 4160 

Funcionario.deinir_novo_aumento(1.1) # A partir daqui o aumento não vai ser mais de 4% e sim e 10%

pedro = Funcionario('Pedro', 5000)
print(pedro.dados()) # 'Pedro' '5000'

pedro.aplicar_aumento()
print(pedro.dados()) # 'Pedro' '5500' 10 %

print(Funcionario.dia_util(minha_data)) # True