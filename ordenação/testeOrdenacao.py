import pytest, ordenador, testeDesempenho

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c=testeDesempenho.Tempo()
        return c.listaQuaseOrdenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c=testeDesempenho.Tempo()
        return c.listaAleatoria(100)
    
    @pytest.fixture
    def esta_ordenada(self,l):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                return False
        return True
    
    @pytest.fixture
    def teste_bolha_curta_aleat(self,o,l_aleat):
        o.NovaBolha(l_aleat)
        return self.esta_ordenada(l_aleat)