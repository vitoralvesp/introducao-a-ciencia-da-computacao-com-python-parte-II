def maiusculas(frase):
    ''' Recebe uma string (Entrada) e retorna uma string (Saída) com todas as letras maiúsculas concatenadas. '''

    string=''

    for letra in frase:
        # UNICODE -> letras maiúsculas de 65 a 90
        if (65<=ord(letra)<=90):
            string+=letra

    return string

