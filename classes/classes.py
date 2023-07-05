# Ex.1: Classe sem a utilização da função init
class Veiculo:
    velocidade_maxima=0
    quilometragem=0

celta=Veiculo()
celta.velocidade_maxima=100
celta.quilometragem=2200
print(celta.velocidade_maxima,celta.quilometragem)


# Ex.2: Classe utilizando a função init
class Veiculo_2:
    def __init__(self,velocidade_maxima=100,quilometragem=0):
        self.velocidade_maxima=velocidade_maxima
        self.quilometragem=quilometragem

civic=Veiculo_2(250,10000)
print(civic.velocidade_maxima,civic.quilometragem)


# Ex.3: Classe sem atribuições
class Veiculo_3:
    pass

Veiculo_3.velocidade_maxima=500
print(Veiculo_3.velocidade_maxima)


# Ex.4: Movie Class
class Movie:
    def __init__(self,score=None,opinion=None):
        self.score = f'{score} stars'
        self.opinion=opinion


killBill=Movie()
killBill.genre='action/drama'
killBill.title='Kill Bill - Vol. 1'
killBill.description='A woman against the world on a path of vengence.'
killBill.director='Quentin Tarantino'
killBill.year='2003'

print(killBill.genre)