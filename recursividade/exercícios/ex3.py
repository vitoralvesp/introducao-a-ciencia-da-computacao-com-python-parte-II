def incomodam(n):
    if (n<1):
        return ''
    else:
        return 'incomodam '+incomodam(n-1)

def elefantes(n):
    if (n<2):
        return ' '
    elif (n==2):
        return f'Um elefante incomoda muita gente\n{n} elefantes incomodam muito mais\n'
    else:
        return f'{elefantes(n-1)}{n-1} elefantes incomodam muita gente\n{n} elefantes {incomodam(n)}muito mais\n'