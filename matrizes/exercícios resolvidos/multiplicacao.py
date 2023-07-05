from criar_matriz import matriz

def multiplicar(a,b):
    ''' Efetua a multiplicação entre duas matrizes A e B '''

    # 1) Restrição: o número de colunas de A deve ser igual ao número de linhas de B
    colunas_a,linhas_a=len(a[0]),len(a)
    colunas_b,linhas_b=len(b[0]),len(b)
    assert (colunas_a==linhas_b), 'O número de colunas em A deve ser igual ao número de linhas em B!'
    

    # 2) Matriz C: possui a relação aij de A e B (os elementos iniciam como zero)
    c=matriz(len(a),len(b[0]))


    # 3) Operação: atribui a soma entre as multiplicações aos elementos da matriz C
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                c[i][j]+=a[i][k]*b[k][j]
    

    return c


# 4) Teste da Função
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
    print('Teste 1: ',teste1) # [[24, 13], [122, 83]]

    matriz_3=[
        [1,2,3],
        [4,5,6]
        ]
    matriz_4=[
        [1,2],
        [3,4],
        [5,6]
        ]
    teste2=multiplicar(matriz_3,matriz_4) 
    print('Teste 2: ',teste2) # [[22, 28], [49, 64]]


