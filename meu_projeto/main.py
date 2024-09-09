from models.pessoa import Pessoa 
from models.enum.sexo import Sexo
from models.endereco import Endereco
import os

os.system("cls||clear")

pessoa_1 =  Pessoa("Lucas",24,Sexo.MASCULINO,
                   Endereco("Rua A", 50))
print(pessoa_1)