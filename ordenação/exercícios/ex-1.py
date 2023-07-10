def ordenada(lista):
    ''' Recebe uma lista como parâmetro e devolve True ou False se está ordenada ou não. '''

    for i in range(len(lista)-1):
        for j in range(i+1,i+2):
            if (lista[i]<lista[j]):
                pass
            else:
                return False
    
    return True
