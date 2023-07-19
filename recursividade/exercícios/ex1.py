def soma_lista(lista):
    ''' Retorna a soma dos elementos de um array inserido pelo usuário utilizando um algoritmo recursivo. '''

    if (len(lista)==0):
        return 0
    else:
        return lista[0]+soma_lista(lista[1:])
    