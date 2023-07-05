from criar_matriz import matriz

def multiplicar(a,b):
    ''' Efetua a multiplicação entre duas matrizes A e B '''

    # 1) Restrições: o número de linhas de A deve ser igual ao número de colunas de B
    # assert (len(a)==len(b[0])), f'Para efetuar uma multiplicação entre matrizes, o número de linhas da 1ª matriz deve ser equivalente ao número de colunas da 2ª matriz.\n\nNúmero de linhas da 1ª matriz: {len(a)}\nNúmero de colunas da 2ª matriz: {len(b[0])}\n'


    # 2) Operação: Cada elemento da matriz A posicionado na linha x multiplica um elemento na posicionado na coluna y da matriz B
    
    c=matriz(len(a),len(b[0]),0)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(c)):
                c[i][j]+=a[i][k]*b[k][j]
    
    return c

if __name__ == '__main__':
    matriz_1=[
        [1,2],
        [8,9]
        ]
    matriz_2=[
        [4,7],
        [10,3]
        ]
    teste1=multiplicar(matriz_1,matriz_2) 
    print(teste1) # [[24, 13], [122, 83]]


    matriz_3=[
        [1,-1,102],
        [2,4,45]
        ]
    matriz_4=[
        [3,7,55],
        [10,2,1]
        ]
    teste2=multiplicar(matriz_3,matriz_4) 
    print(teste2) # [[-7, 5, 54], [46, 22, 114]]


