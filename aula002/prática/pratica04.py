from sunau import Au_read


base = int(input('Digite a base do retangulo: '))
altura = int(input('Digite a altura do retangulo: '))

perimetro = 2 * (base + altura)
area = base * altura

print('O perímetro do seu retangulo é:', perimetro, 'e a área do seu retangulo é:', area)