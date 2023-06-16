def soma_matrizes(m1,m2):
    ''' (m1,m2) -> soma_matrizes(m1 + m2)
    Efetua a soma de um elemento A da matriz m1 
    com um elemento B na matriz m2 se, e somente se, as suas
    dimensoes forem equivalentes.
    '''

    # verificação entre as dimensoes das matrizes
    for linha_m1,linha_m2 in zip(m1,m2):
        if (len(linha_m1)==len(linha_m2)):
            continue
        else:
            return False

    # efetua a soma dos elementos das matrizes
    m3=[]
    for j in range(len(m1)):
        trash=[]
        for i in range(len(m1[j])):
            trash.append(m1[j][i]+m2[j][i])
        m3.append(trash[:])
        trash.clear()
    
    return m3
