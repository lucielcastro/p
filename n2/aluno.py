from curso import Curso
from pessoa_fisica import Pessoa_fisica


class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.matricula=matricula
      self.ano_ingresso=ano_ingresso
   
'''   def matricular_aluno(self,nome: str, matricula:str, ano_ingresso: int):
      alunos=[]
      alunos.append(Aluno(nome=nome, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Matricular aluno:\n\n')
      for alun in self.alunos:
         alun.nome = input('Informe nome:')
         alun.matricula = input('Informe matricula')
         alun.ano_ingresso = int(input('Informe ano de ingresso:'))
         print(alun)'''

A