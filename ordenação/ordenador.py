class Ordenador:
    def selecaoDireta(self,lista,reverse=False):
        ''' (list,True/False) -> Compara o maior ou menor elemento entre um elemento da lista e seu sucessor, reorganizando a lista.  '''

        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if (reverse==True) and (lista[i]<lista[j]):
                    lista[i],lista[j]=lista[j],lista[i]
                else:
                    if (lista[j]<lista[i]):
                        lista[j],lista[i]=lista[i],lista[j]


    def bolha(self,lista):
        ''' Algoritmo de Ordenação Bubble Sort '''

        fim=len(lista)
        for i in range(fim-1,0,-1):
            for j in range(i):
                if (lista[j]>lista[j+1]):
                    lista[j],lista[j+1]=lista[j+1],lista[j]
        


if __name__=='__main__':

    x=Ordenador()
    y=Ordenador()

    lista=[5,3,1,2,7,6] # Lista com os elementos sem uma ordem definida

    x.selecaoDireta(lista) 
    print('Seleção Direta: ',lista) # Lista Ordenada Crescentemente: [1, 2, 3, 5, 6, 7]
    y.selecaoDireta(lista,True) 
    print('Seleção Direta: ',lista) # Lista Ordenada Decrescentemente: [7, 6, 5, 3, 2, 1]

    # -------- 

    z=Ordenador()
    lista_2=[2,3,7,0,9,-1]
    z.bolha(lista_2)
    print('\nBubble Sort: ',lista_2)

