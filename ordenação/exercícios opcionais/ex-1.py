from random import randint

def lista_grande(n):
    ''' Retorna uma lista de tamanho n com n números inteiros. '''

    lista=list()
    for _ in range(n):
        lista.append(randint(0,10))

    return lista
    
