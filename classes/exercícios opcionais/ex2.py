class Triangulo:
    ''' Classe construtora do Triângulo
        Descrição: um triângulo é uma figura geométrica plana que possui três lados. '''

    def __init__(self,a,b,c):
        ''' Função construtora da Classe Triângulo. '''

        self.a=a
        self.b=b
        self.c=c
    

    def perimetro(self):
        ''' Retorna o cálculo do perímetro de um triângulo. '''
        return (self.a)+(self.b)+(self.c)
    

    def retangulo(self):
        ''' Retorna Verdadeiro se um triângulo é retângulo e Falso se um triângulo não é retângulo. '''

        lista=[self.a,self.b,self.c]
        lista.sort(reverse=True) # organiza os elementos do array de acordo com o Teorema de Pitágoras

        # Restrição: as medidas dos lados devem obedecer ao Teorema de Pitágoras (a soma dos quadrados de seus catetos equivalem ao quadrado da hipotenusa).
        if (lista[0]**2)==(lista[1]**2+lista[2]**2):
            return True
        else:
            return False


    def semelhantes(self,triangulo):
        ''' Retorna Verdadeiro se um triângulo é semelhante ou Falso se um triângulo não é semelhante. '''

        self.triangulo=triangulo


        lista1=[self.a,self.b,self.c]
        lista2=[triangulo.a,triangulo.b,triangulo.c]
        lista3=list()


        # Operação entre os elementos no Array
        if (sum(lista1)>sum(lista2)):
            for elemento1,elemento2 in zip(lista1,lista2):
                lista3.append(elemento1/elemento2)
        else:
            for elemento1,elemento2 in zip(lista2,lista1):
                lista3.append(elemento1/elemento2)
        

        # Razão de Proporcionalidade
        if (lista3[0]==lista3[1]==lista3[2]):
            return True
        else:
            return False

