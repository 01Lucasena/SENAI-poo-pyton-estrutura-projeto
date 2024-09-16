import pytest
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enum.sexo import Sexo
from models.enum.uf import Unidade_federativa

@pytest.fixture
def criar_pessoa():
    pessoa_1 =  Pessoa("Lucas",24,Sexo.MASCULINO,
                   Endereco("Rua A", 50, "Salvador", Unidade_federativa.BAHIA))
    
    return pessoa_1

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.nome == "Lucas"
