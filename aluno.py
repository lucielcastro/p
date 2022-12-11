
from pessoa_fisica import Curso, Pessoa_fisica

class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, curso:Curso, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.curso = curso
      self.matricula = matricula
      self.ano_ingresso = ano_ingresso
      self.alunos = []
      curso = Curso.cadastrar_curso()

   def cadastrar_aluno(self, nome, curso, matricula, ano_ingresso):
      self.alunos.append(Aluno(nome=nome, curso=curso, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Aluno cadastrado com sucesso!')
   

   def consultar_alunos(self):
      print('\n**** ALUNOS CADASTRADo ****')
      for aluno in self.alunos:
         print(f'{aluno.nome} {aluno.curso} {aluno.matricula}')
   
op2=1
while op2 !=0:
   print('\n*********** MANTER ALUNO ***********')
   print('#  1-Cadastrar\n#  2-Editar\n#  3-Deletar\n#  4-Consultar \n#  0-Sair')
   print('####################################')
   op2=int(input('\nInforme uma das opcoes acima: '))

   if op2 == 1:
      print('\n********** CADASTRAR ALUNO **********')
      name = input('Informe nome: ')
      #imprimir_cursos_disponiveis()
      curso = input('Informe curso: ')
      #curso_buscado = verificar_cursos(curso)
      curso_busca = Curso.consultar_cursos()
      mat = input('Infome matricula: ')
      ano_ing = input('Informe ano ingresso: ')
      aluno = Aluno(name, curso_busca, mat, ano_ing)
      aluno.cadastrar_aluno(name, curso, mat, ano_ing)
      print(f'Nome: {aluno.nome}\nCurso: {aluno.curso}\nMatricula: {aluno.matricula}\nAno de ingresso: {aluno.ano_ingresso}')
      
   elif op2 == 4:
      aluno.consultar_alunos()
   '''
   elif op2 == 2:
      nome = input('Informe nome: ')
      aluno_busca = editar_aluno(nome)'''





















'''from curso import Curso
from pessoa_fisica import Pessoa_fisica


class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.matricula=matricula
      self.ano_ingresso=ano_ingresso
     def matricular_aluno(self,nome: str, matricula:str, ano_ingresso: int):
      alunos=[]
      alunos.append(Aluno(nome=nome, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Matricular aluno:\n\n')
      for alun in self.alunos:
         alun.nome = input('Informe nome:')
         alun.matricula = input('Informe matricula')
         alun.ano_ingresso = int(input('Informe ano de ingresso:'))
         print(alun)'''