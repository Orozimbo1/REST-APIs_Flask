# "args" ==> arguments (argumentos)
# "kwargs" ==> keyword arguments (argumentos de palavras-chave)

def soma(*args): # Quando não se tem a quantidade exata de argumentos, trata-se como um lista
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3, 4, 5, 6)) # 69

def kwargs(*args, **kwargs):# Sempre por args antes de kwargs
    print(args)
    print(kwargs)

kwargs(1,3, nome="ana")# args => (1, 3) e kwargs => {'nome': 'ana'} / kwargs sempre retornam dicionário