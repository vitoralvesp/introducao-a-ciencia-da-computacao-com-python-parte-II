class Ordenador:
    def bubbleSort(self,lista,reverse=False):
        ''' (list,True/False) -> Compara o maior ou menor elemento entre um elemento da lista e seu sucessor, reorganizando a lista.  '''

        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if (reverse==True) and (lista[i]<lista[j]):
                    lista[i],lista[j]=lista[j],lista[i]
                else:
                    if (lista[j]<lista[i]):
                        lista[j],lista[i]=lista[i],lista[j]

        return lista


if __name__=='__main__':

    x=Ordenador()
    y=Ordenador()

    lista=[5,3,1,2,7,6] # Lista com os elementos sem uma ordem definida
    x.bubbleSort(lista) # Lista Ordenada Crescentemente: [1, 2, 3, 5, 6, 7]
    y.bubbleSort(lista,True) # Lista Ordenada Decrescentemente: [7, 6, 5, 3, 2, 1]
