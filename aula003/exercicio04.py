from datetime import date
current_date = date.today()
anoatual = current_date.year
anonasc = int(input('Digite seu ano de nascimento: '))

if (anoatual - anonasc) >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')