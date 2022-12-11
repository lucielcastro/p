
cursos = []
alunos = []

def editar_aluno( nome):
      for aluno in alunos:
         if nome == aluno.nome:
            print(aluno)
            print('Qual dados deseja editar?\n\n1-todos')
            op = int(input('Inorme:'))
            if op == 1:
               aluno.nome = input('Nome:')
               aluno.curso = input('Curso:')
               aluno.matricula = input('Matricula:')
               aluno.ano_ingresso = int(input('Ano ingresso:'))
               return aluno.nome, aluno.curso, aluno.matricula, aluno.ano_ingresso
               #print(f'Dados atualizados: {aluno}')
         print('Aluno não encontrado na base de dados')
         encontrar_aluno = input('Informe nome novamente:')
         editar_aluno(encontrar_aluno)

def imprimir_cursos_disponiveis():
   for curso in cursos:
      print('CURSOS DISPONIVEIS:')
      print(curso.nome)

def verificar_cursos( curso: str):
   for curs in cursos:
      if curso == curs.nome:
         #alunos_curso[curs.nome] = dados_aluno
         return curs.nome
   print('Curso não cadastrado')
   imprimir_cursos_disponiveis()
   encontrar_curso = input('Informe um curso:')
   verificar_cursos(encontrar_curso)
   return curs.nome
   
class Pessoa_fisica:
   def __init__(self, nome: str):
      self.nome=nome

class Aluno(Pessoa_fisica):
   def __init__(self, nome: str, curso, matricula: str, ano_ingresso: int):
      super().__init__( nome)
      self.curso=curso
      self.matricula=matricula
      self.ano_ingresso=ano_ingresso
   
   def cadastrar_aluno(self, nome, curso, matricula, ano_ingresso):
      alunos.append(Aluno(nome=nome, curso=curso, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Aluno cadastrado com sucesso!')
   

   def imprimir_alunos(self):
      print('\n**** ALUNOS CADASTRADo ****')
      for aluno in alunos:
         print(f'{aluno.nome} {aluno.curso} {aluno.matricula}')

class Curso:
   def __init__(self,nome: str, descricao: str):
      self.nome = nome
      self.descricao = descricao
      self.alunos = []
   
   def cadastrar_curso(self, nome, descricao):
      cursos.append(Curso(nome=nome, descricao=descricao))
      print('Curso cadastrado com sucesso!')
   
   def consultar_cursos(self):
      print('\n**** CURSOS DISPONIVÉIS ****')
      for curso in cursos:
         print(curso.nome)

   def matricular_aluno(self, nome, curso, matricula, ano_ingresso):
      self.alunos.append(Aluno(nome=nome, curso=curso, matricula=matricula, ano_ingresso=ano_ingresso))
      print('Aluno matriculado com sucesso!')

   def impri_alunos(self):
      print('\n**** ALUNOS MATRICULADOS ****')
      for aluno in self.alunos:
         print(aluno.nome)

'''if not cursos:
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
         print(f'{c.nome} {c.descricao}')'''
def v(curso):
   if len(cursos)==0:
      print('\nATENCAO:\nNao ha cursos cadastrados no sistema. Cadastre o curso que será ofertado para o aluno.\n')
      print('\n********** CADASTRAR CURSO **********')
      name = input('Informe nome: ')
      descric = input('Infome descricao: ')
      c = Curso(name, descric)
      c.cadastrar_curso(name, descric)
      print(f'{c.nome} {c.descricao}')
      return c
   else:
      verificar_cursos(curso)

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
      curso_busca = v(curso)
      mat = input('Infome matricula: ')
      ano_ing = input('Informe ano ingresso: ')
      aluno = Aluno(name, curso_busca, mat, ano_ing)
      aluno.cadastrar_aluno(name, curso, mat, ano_ing)
      print(f'Nome: {aluno.nome}\nCurso: {aluno.curso}\nMatricula: {aluno.matricula}\nAno de ingresso: {aluno.ano_ingresso}')
   elif op2 == 2:
      nome = input('Informe nome: ')
      aluno_busca = editar_aluno(nome)
      
   elif op2 == 4:
      aluno.imprimir_alunos()
   
   elif op2 == 5:
      print('\n****** CADASTRAR CURSO ******')
      name = input('Informe nome: ')
      descric = input('Infome descricao: ')
      c = Curso(name, descric)
      c.cadastrar_curso(name, descric)
      print(f'{c.nome} {c.descricao}')
   
   elif op2 == 6:
      c.consultar_cursos()

   '''  if op2 == 1:
      print('\n****** MATRICULAR ALUNO ******')
      name = input('Informe nome: ')
      #imprimir_cursos_disponiveis()
      curso = input('Informe curso: ')
      #curso_buscado = verificar_cursos(curso)
      mat = input('Infome matricula: ')
      ano_ing = input('Informe ano ingresso: ')
      aluno = Aluno(name, curso, mat, ano_ing)
      aluno.matricular_aluno(name, curso, mat, ano_ing)
      print(f'Nome: {aluno.nome}\nCurso: {aluno.curso}\nMatricula: {aluno.matricula}\nAno de ingresso: {aluno.ano_ingresso}')'''




      
      



  







