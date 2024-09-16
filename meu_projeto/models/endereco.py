from enum.uf import Unidade_federativa
class Endereco:
    
    def __init__(self, logradouro:str, numero:int, cidade:str, unidade_federativa: Unidade_federativa ) -> None:
       self.logradouro = logradouro
       self.numero = numero
       self.cidade = cidade
       self.unidade_federativa = unidade_federativa

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nCidade: {self.cidade}"    
            f"\nUnidade Federativa: {self.unidade_federativa}"    
                )