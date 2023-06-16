def dimensoes(minha_matriz):
    ''' (minha_linha) -> dimensao(linha e coluna)
    Analisa uma matriz adicionada como parâmetro pelo usuário 
    e retorna a quantidade i de linhas e j de colunas.
    '''

    qtd_lin=0
    qtd_col=0

    
    # contabiliza o número total de linhas
    for _ in range(len(minha_matriz)):
        qtd_lin+=1

    # contabiliza o número total de colunas
    for _ in range(len(minha_matriz[0])):
        qtd_col+=1
    

    print(f'{qtd_lin}x{qtd_col}')
