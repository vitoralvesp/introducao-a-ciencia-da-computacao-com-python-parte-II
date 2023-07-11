class Ordenador:
    def selecaoDireta(self,lista,reverse=False):
        ''' (list,True/False) -> Compara o maior ou menor elemento entre um elemento da lista e seu sucessor, reorganizando a lista. '''

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

    
    def NovaBolha(self,lista):
        ''' Otimização no Algoritmo de Ordenação Bubble Sort '''

        fim=len(lista)

        for i in range(fim-1,0,-1):
            trocou=False
            
            for j in range(i):
                if (lista[j]>lista[j+1]):
                    lista[j],lista[j+1]=lista[j+1],lista[j]
                    trocou=True

            if not trocou:
                return

