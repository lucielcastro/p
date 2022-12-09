

alunos = []
cursos = []
alunos_curso = {}

def imprimir_cursos_disponiveis():
   for curso in cursos:
      print('CURSOS DISPONIVEIS:')
      print(curso.nome)

def verificar_cursos( curso: str):
   for curs in cursos:
      if curso == curs.nome:
         '''alunos_curso[curs.nome] = dados_aluno'''
         return curs.nome
   print('Curso não cadastrado')
   encontrar_curso = input('Informe curso:')
   verificar_cursos(encontrar_curso)
   return curs

class Pessoa_fisica:
   def __init__(self, nome: str):
      self.nome=nome

class Curso:
   def __init__(self,nome: str, descricao: str):
      self.nome = nome
      self.descricao = descricao
   
   def cadastrar_curso(self, nome, descricao):
      cursos.append(Curso(nome=nome, descricao=descricao))
      print('Curso cadastrado com sucesso!')
   
   def consultar_cursos(self):
      print('\n**** CURSOS DISPONIVÉIS ****')
      for curso in cursos:
         print(curso.nome)
      
class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, curso: Curso, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.matricula=matricula
      self.ano_ingresso=ano_ingresso
      self.curso=curso

   def matricular_aluno(self, nome, curso, matricula, ano_ingresso):
      alunos.append(Aluno(nome=nome, curso=curso, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Aluno matriculado com sucesso!')

   def imprimir_alunos(self):
      print('\n**** ALUNOS MATRICULADOS ****')
      for aluno in alunos:
         print(aluno.nome)

if not cursos:
   print('\nATENCAO:\n\nNao ha cursos cadastrados no sistema. Cadastre os cursos que serão ofertados na instituicao.\n')
   op = 1
   while op !=0:
      print('\n******************************************************')
      print('1-Cadastrar Curso\n0-Sair')
      print('\n******************************************************')
      op=int(input('\nInforme uma das opcoes acima: '))
   
      if op == 1:
         print('\n****** CADASTRAR CURSO ******')
         name = input('Informe nome: ')
         descric = input('Infome descricao: ')
         c = Curso(name, descric)
         c.cadastrar_curso(name, descric)
         print(f'{c.nome} {c.descricao}')

op2=1
while op2 !=0:
   print('\n##################################')
   print('#  1-Matricular aluno\n#  2-Consultar Alunos Matriculados\n#  3-Cadastrar Curso\n#  4-Consultar Cursos\n#  0-Sair')
   print('##################################')
   op2=int(input('\nInforme uma das opcoes acima: '))

   if op2 == 1:
      print('\n****** MATRICULAR ALUNO ******')
      name = input('Informe nome: ')
      imprimir_cursos_disponiveis()
      curso = input('Informe curso: ')
      curso_buscado = verificar_cursos(curso)
      mat = input('Infome matricula: ')
      ano_ing = input('Informe ano ingresso: ')
      a = Aluno(name, curso_buscado, mat, ano_ing)
      a.matricular_aluno(name, curso_buscado, mat, ano_ing)
      print(f'Nome: {a.nome}\nCurso: {a.curso}\nMatricula: {a.matricula}\nAno de ingresso: {a.ano_ingresso}')
   
   elif op2 == 2:
      a.imprimir_alunos()
   
   elif op2 == 3:
      print('\n****** CADASTRAR CURSO ******')
      name = input('Informe nome: ')
      descric = input('Infome descricao: ')
      c = Curso(name, descric)
      c.cadastrar_curso(name, descric)
      print(f'{c.nome} {c.descricao}')
   
   elif op2 == 4:
      c.consultar_cursos()




      
      



  







