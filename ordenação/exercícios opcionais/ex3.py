def insertion_sort(lista):
    ''' Ordena os elementos de um array em ordem crescente utilizando o Algoritmo de Ordenação Insertion Sort '''


    for i in range(1,len(lista)):

        key=lista[i]
        j=i-1

        while (j>=0) and (key<lista[j]):
            lista[j+1]=lista[j]
            j-=1
        
        lista[j+1]=key


    return lista

