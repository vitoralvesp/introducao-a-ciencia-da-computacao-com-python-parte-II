def imprime_matriz(matriz):
    ''' (matriz) -> imprime_matriz(linha a linha)
    Recebe uma matriz como parâmetro e imprime cada linha
    do array.
    '''

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna],end=' ')
        print('\n',end='')