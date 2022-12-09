
from pessoa_fisica import Pessoa_fisica

class Professor(Pessoa_fisica):
   def __init__(self, nome: str, salario: float, formacao: str):
      super().__init__( nome)
      self.salario=salario
      self.formacao=formacao