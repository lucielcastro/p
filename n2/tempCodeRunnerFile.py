 if op == 1:
      print('\n****** MATRICULAR ALUNO ******')
      name = input('Informe nome: ')
      curso = input('Informe curso')
      mat = input('Infome matricula: ')
      ano_ing = input('Informe ano ingresso: ')
      a = Aluno(name, mat , ano_ing)
      a.matricular_aluno(name,mat, ano_ing)
      print(f'{a.nome} {a.matricula} {a.ano_ingresso}')

   elif op == 2:
      a.imprimir_alunos()