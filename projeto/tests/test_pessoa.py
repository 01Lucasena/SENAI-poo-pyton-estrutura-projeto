import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.uf import Unidade_federativa

@pytest.fixture
def criar_pessoa():
    pessoa_1 =  Pessoa("Lucas",24,Sexo.MASCULINO,
                   Endereco("Rua A", 50, "Salvador", Unidade_federativa.BAHIA))
    
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Lucas"
