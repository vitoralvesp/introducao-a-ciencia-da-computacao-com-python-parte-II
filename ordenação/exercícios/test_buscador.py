import ex3,pytest

class TestBuscador:

    @pytest.fixture
    def buscador(self):
        return ex3.Buscador()
        
    def test_vogais(self,buscador):
        vogais=['a','e','i']
        assert buscador.BuscaBinaria(vogais,"e") == 1
        
    def test_numeros1(self,buscador):
        numeros1=[1,2,3,4,5]
        assert buscador.BuscaBinaria(numeros1,6) == False 
        
    def test_numeros2(self,buscador):
        numeros2=[1,2,3,4,5,6]
        assert buscador.BuscaBinaria(numeros2,4) == 3