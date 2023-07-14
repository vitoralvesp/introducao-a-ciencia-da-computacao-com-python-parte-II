def busca(lista,elemento):
    ''' Retorna o índice de um elemento caso exista no array.
        Se não estiver, retorna False. '''
        
    primeiro=0
    ultimo=len(lista)-1

    while (primeiro<=ultimo):
        meio=(primeiro+ultimo)//2
        print(meio)

        if (lista[meio]==elemento):
            return meio
        else:
            if (elemento<lista[meio]):
                ultimo=meio-1
            else:
                primeiro=meio+1
        
    return False

# print(busca(['a','e','i'],'e'))
# print(busca([1,2,3,4,5],6))
# print(busca([1,2,3,4,5,6],4))
# print(busca([1,2,3,4,5,6],4))



    

