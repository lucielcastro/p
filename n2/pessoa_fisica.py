
cursos = []
alunos = []

class Pessoa_fisica:
   def __init__(self, nome: str):
      self.nome=nome

class Curso:
   def __init__(self,nome: str, descricao: str):
      self.nome = nome
      self.descricao = descricao
  
   
   def cadastrar_curso(self, nome, descricao):
      cursos.append(Curso(nome, descricao))
      for curso in cursos:
         curso.nome = input('Informe nome:')
         curso.descricao = input('Descricao do curso:')
         cursos.append(curso)
   
   def matricular_aluno(self, nome, matricula, ano_ingresso):
      self.alunos.append(Aluno(nome, matricula,ano_ingresso))
      for aluno in self.alunos:
         aluno.nome

class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.matricula=matricula
      self.ano_ingresso=ano_ingresso






