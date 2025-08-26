media = float(input('Digite a média do aluno: '))
if media >= 5: 
    print('A média informada é: ', media, 'Aluno foi Aprovado!')
elif media >= 4 and media <= 4.5:
    print('A média informada é:', media, 'O aluno ficou de recuperação')
else:
    print('A media informada é: ', media, 'Aluno foi reprovado')