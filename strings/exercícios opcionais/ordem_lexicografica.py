def primeiro_lex(lista):
    ''' Compara os elementos de um array e retorna o maior valor entre eles. '''

    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if (lista[j]>lista[j+1]):
                lista[j],lista[j+1]=lista[j+1],lista[j]
    
    return lista[0]