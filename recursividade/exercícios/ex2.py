def encontra_impares(lista):
    ''' Retorna um array com todos os elementos ímpares presentes no array inserido como parâmetro utilizando um algoritmo recursivo. '''

    if (len(lista)==0):
        return []

    if (lista[0]%2!=0):
        return [lista[0]]+encontra_impares(lista[1:])
    
    return encontra_impares(lista[1:])

