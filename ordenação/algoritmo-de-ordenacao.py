class Ordenador:
    def bubbleSort(self,lista,reverse=False):

        for i in range(len(lista)-1):
            for j in range(i+1,len(lista)):
                if (reverse==True) and (lista[i]<lista[j]):
                    lista[i],lista[j]=lista[j],lista[i]
                else:
                    if (lista[j]<lista[i]):
                        lista[j],lista[i]=lista[i],lista[j]

        print(lista)

lista=[5,3,1,2,7,6]
x=Ordenador()
y=Ordenador()
x.bubbleSort(lista) # [1, 2, 3, 5, 6, 7]
y.bubbleSort(lista,True) # [7, 6, 5, 3, 2, 1]
