def sao_multiplicaveis(m1,m2):
    ''' (m1,m2) -> sao_multiplicaveis(duas matrizes)
    Recebe duas matrizes como parâmetro e retorna Verdadeiro
    se o número total de colunas de m1 forem equivalentes ao
    número de linhas de m2 (são multiplicáveis).
    '''

    col_m1=0
    lin_m2=0

    # contabiliza o número total de colunas em m1
    for _ in m1[0]:
        col_m1+=1

    # contabiliza o número total de linhas em m2
    for _ in m2:
        lin_m2+=1
    
    if (col_m1==lin_m2):
        return True
    else:
        return False