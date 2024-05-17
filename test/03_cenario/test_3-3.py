import pytest

# Adicione a opção --capture ao pytest
pytest.main("--capture")


def test_3_3_igualdade_15():
    print('1º passo do teste')
    print('2º passo do teste')
    print('3º passo do teste')
    print('4º passo do teste')
    assert 15 == 15    