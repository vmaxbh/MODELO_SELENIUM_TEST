import pytest

# Adicione a opção --capture ao pytest
pytest.main("--capture")


def test_2_1_igualdade_10():
    print('1º passo do teste feito com Sucesso!')
    print('2º passo do teste feito com Sucesso!')
    print('3º passo do teste feito com Sucesso!')
    print('4º passo do teste feito com Sucesso!')
    assert 10 == 10    