idade = int(input("Insira a idade do Nadador: "))

if idade >= 5 & idade <= 7:
    print("O nadador pertence a categoria Infantil A!")
elif idade <= 11: 
    print("O nadador pertence a categoria Infantil B!")
elif idade <= 13: 
    print("O nadador pertence a categoria Juvenil A!")
elif idade <= 17:
    print("O nadador pertence a categoria Juvenil B!")
else:
    print("O nadador pertence a categoria Adultos!")
    