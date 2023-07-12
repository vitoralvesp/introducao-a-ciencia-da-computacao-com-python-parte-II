import random, ordenador, time

class Tempo:
    def listaAleatoria(self,n):
        ''' Cria uma lista com elementos aleatórios de tamanho n '''
        
        lista=[random.randrange(1000) for _ in range(n)] # adiciona elementos aleatórios de 0 a 999 em n posições
        
        return lista
    

    def listaQuaseOrdenada(self,n):
        ''' Cria uma lista com elementos ordenados até a metade do seu tamanho. '''

        lista=[x for x in range(n)] # adiciona elementos ordenados de 0 a n em n posições

        lista[n//10]=-500 # adiciona -500 na 10ª posição

        return lista


    def compara(self,n):
        lista1=self.listaAleatoria(n)
        lista2=lista1[:]
        lista3=lista2[:]
        listaQuaseOrdenada=self.listaQuaseOrdenada(n)

        o=ordenador.Ordenador()

        # Seleção Direta
        antes=time.time()
        o.selecaoDireta(lista1)
        depois=time.time()
        print(f'Seleção Direta: {depois-antes}sec')

        # Bubble Sort
        antes=time.time()
        o.bolha(lista2)
        depois=time.time()
        print(f'BubbleSort: {depois-antes}sec')

        # (Update) Bubble Sort
        antes=time.time()
        o.NovaBolha(lista3)
        depois=time.time()
        print(f'(Update) BubbleSort: {depois-antes}sec')

        # Bubble Sort com uma lista quase ordenada
        antes=time.time()
        o.NovaBolha(listaQuaseOrdenada)
        depois=time.time()
        print(f'(Lista quase ordenada) BubbleSort: {depois-antes}sec')


if __name__=='__main__':

    # 1º Caso: vetores de tamanho 1000
    a=Tempo()
    a.compara(1000)

    print()

    # 2º Caso: vetores de tamanho 100
    b=Tempo()
    b.compara(100)

    print()

    # 3º Caso: vetores de tamanho 10
    c=Tempo()
    c.compara(10)
    

