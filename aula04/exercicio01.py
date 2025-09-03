time1 = float(input('Quantos gols marcou o time 1?: '))
time2 = float(input('Quantos gols marcou o time 2?: '))

if time1 > time2:
    print("O time 1 ganhou o jogo.")
elif  time1 == time2:
    print("O jogo foi um empate.")
else:
    print("O time 2 ganhou o jogo.")    