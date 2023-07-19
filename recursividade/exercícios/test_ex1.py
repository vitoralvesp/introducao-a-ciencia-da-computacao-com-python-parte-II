from ex1 import soma_lista
import pytest

@pytest.mark.parametrize('lista,esperado', [
    ([1,2],3)
])

def test_soma_lista(lista,esperado):
    assert (soma_lista(lista)==esperado), f'O valor esperado era {esperado}, mas retornou {soma_lista(lista)}...'