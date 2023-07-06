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
