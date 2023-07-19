from ex1 import soma_lista
import pytest

@pytest.mark.parametrize('lista,esperado', [
    ([1,2],3),
    ([1,2,3],6),
    ([1,2,3,4],10),
    ([1,2,3,4,5],15),
    ([5,5,5,5],20)
])

def test_soma_lista(lista,esperado):
    assert (soma_lista(lista)==esperado), f'O valor esperado era {esperado}, mas retornou {soma_lista(lista)}...'