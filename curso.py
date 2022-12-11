'''

class Disciplina:
   def __init__(self, nome: str, carga_horaria: int, descricao: str, semestre: str, ano: int):
      self.nome = nome
      self.carga_horaria = carga_horaria
      self.descricao = descricao
      self.semestre = semestre
      self.ano = ano
   
cursos = []
class Curso:
   def __init__(self,nome: str, descricao: str):
      self.nome = nome
      self.descricao = descricao
      self.alunos = []
   
   def cadastrar_curso(self, nome, descricao):
      cursos.append(Curso(nome, descricao))
      for curso in cursos:
         curso.nome = input('Informe nome:')
         curso.descricao = input('Descricao do curso:')
         cursos.append(curso)
   def matricular_aluno(self, ):
      self.alunos.append(Aluno())
      
   def imprimir_dados_curso(self)-> None:
      for curso in self.cursos:
         print(f'Cursos: {curso}')

   def listar_cursos(self):
      print(f'{self.cursos[0]}')'''
'''
n = input('informe nome:')
d = input('Informe descricao')'''

         
      

   