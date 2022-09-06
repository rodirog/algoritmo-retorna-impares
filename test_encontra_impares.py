import pytest
from encontra_impares import Recursao

exemplo_recursao = Recursao()

@pytest.mark.parametrize("entrada, esperado",[
    ([2,3,4,5,6],[3,5]),
    ([3],[3]),
    ([2],[]),
    ([6,8,88],[]),
    ([57,3,17,9,101],[57,3,17,9,101])
])

def testa_encontra_impares(entrada,esperado):

    assert exemplo_recursao.encontra_impares(entrada) == esperado
