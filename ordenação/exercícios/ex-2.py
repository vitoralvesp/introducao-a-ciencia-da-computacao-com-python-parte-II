def busca(lista,elemento):
    ''' (list, int/str/float) -> Recebe um array de elementos e retorna o índice do elemento especificado como parâmentro se estiver no array e False caso contrário. '''

    # Solução 1: 
    # return lista.index(elemento) if (elemento in lista) else False

    # Solução 2:
    for i in range(len(lista)):
        if (elemento==lista[i]):
            return i
    return False