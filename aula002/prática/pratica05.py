valor = int(input('Insira o valor inicial da sua prestação: '))
taxa = int(input('Insira o valor da taxa de juros da prestação: '))
tempo = int(input('Insira a quantidade de meses que a prestação está em atraso: '))

prestacao = valor + (valor * (taxa/100) * tempo)

print('O valor da sua prestação está em:', prestacao)