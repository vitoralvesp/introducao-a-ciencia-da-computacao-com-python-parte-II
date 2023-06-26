def menor_nome(nomes):
    ''' Recebe uma lista de nomes e retorna o menor nome na lista. '''

    # loop para a formatação dos nomes na lista
    nomes=[nome.strip().lower().capitalize() for nome in nomes]

    # menorNome -> inicialmente, recebe o primeiro valor da lista
    menorNome=nomes[0]

    # menorNome -> recebe nome se len(nome) for menor que len(menorNome)
    for nome in nomes:
        if len(menorNome)>len(nome):
            menorNome=nome

    # retorna o menor nome na lista.
    return menorNome