import random, ordenador, time

class Tempo:
    def listaAleatoria(self,n):
        ''' Cria uma lista com elementos aleatórios de tamanho n '''
        
        lista=[0 for x in range(n)] # adiciona elementos 0 em n posições

        for i in range(n):
            lista[i]=random.randrange(1000) # int entre 0 e 999
        
        return lista


    def compara(self,n):
        lista1=self.listaAleatoria(n)
        lista2=lista1[:]

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
    

