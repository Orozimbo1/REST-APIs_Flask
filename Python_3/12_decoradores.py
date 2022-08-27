import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print('*******EMBRULHANDO FUNCAO NO DECORADOR*********')
        funcao()
        print('*********FECHANDO EMBRULHO**********')
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print('Eu sou uma funcao!')

minha_funcao()