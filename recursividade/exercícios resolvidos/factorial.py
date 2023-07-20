import pytest

def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
    

@pytest.mark.parametrize("numero,esperado", [
    (5,120),
    (4,24),
    (3,6)
])
def test_factorial(numero,esperado):
    assert (factorial(numero)==esperado)