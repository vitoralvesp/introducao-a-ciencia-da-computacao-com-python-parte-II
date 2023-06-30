def matriz(linhas,colunas,elemento):
    ''' Cria uma matriz com x linhas, y colunas e z elementos, especificados pelo usuário. '''

    matriz=list() # cria uma lista vazia
    
    for _ in range(linhas): 
        linha_i=[] # Ex: []
        for _ in range(colunas):
            linha_i.append(elemento) # Ex: [0,0,...]
        
        matriz.append(linha_i) # Ex: [[0,0,0],...]
    
    return matriz


def somar(x,y):
    ''' Retorna a soma de duas matrizes x e y. '''

    linhas=len(x)
    colunas=len(x[0])

    novaMatriz=matriz(linhas,colunas,0) # [[0,0,0],[0,0,0],[0,0,0]]

    for linha in range(linhas):
        for coluna in range(colunas):
            novaMatriz[linha][coluna]=x[linha][coluna]+y[linha][coluna] # Reescreve o elemento 0 por x_elemento + y_elemento
    
    return novaMatriz


if __name__ == '__main__':
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[10,20,30],[40,50,60],[70,80,90]]
    print(somar(a,b)) # [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

    c=[[2,2],[8,9]]
    d=[[12,33],[9,0]]
    print(somar(c,d)) # [[14, 35], [17, 9]]

