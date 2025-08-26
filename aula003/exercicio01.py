nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))

media = nota1 + nota2 / 2

if media >= 6:
    print('Aluno está aprovado')
else:
    print("Aluno não foi aprovado")