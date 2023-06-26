def conta_letras(frase,contar='vogais'):
    ''' Retorna o total de vogais ou consoantes em uma string. '''

    vogais_=["a","e","i","o","u"]
    consoantes_=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

    if (contar=='vogais'):
        vogais=0
        
        for letra in frase:
            if letra in vogais_:
                vogais+=1
            
        return vogais
    
    else:
        consoantes=0
        
        for letra in frase:
            if letra in consoantes_:
                consoantes+=1
        
        return consoantes    
