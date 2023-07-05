def matriz(linhas,colunas,elemento=0):
    ''' Cria uma matriz com x linhas, y colunas e z elementos, especificados pelo usuário. '''

    matriz=list() # cria uma lista vazia
    
    for _ in range(linhas): 
        linha_i=[] # Ex: []
        for _ in range(colunas):
            linha_i.append(elemento) # Ex: [0,0,...]
        
        matriz.append(linha_i) # Ex: [[0,0,0],...]
    
    return matriz