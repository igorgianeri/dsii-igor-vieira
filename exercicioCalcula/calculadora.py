import math

def calc():
    print("Calculadora Muito Divertida- Feita por Eduardo Romanini Pessoa")
    
    while True:
        print("\nMenu:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potenciação (^)")
        print("6. Raiz Quadrada (√)")
        print("7. Pi (π)")
        print("8. Tangente (tan)")
        print("9. Cosseno (cos)")
        print("10. Seno (sin)")
        print("11. Logaritmo (log)")
        print("12. Fatorial (fatorial)")
        print("13. Sair")

        escolha = input("Digite o número presente na frente da operação desejada: ")

        if escolha == '1':  # Adição
            num1 = float(input('Informe seu primeiro número: '))
            num2 = float(input('Informe seu segundo número: '))
            print(f"Resultado da Adição: {num1 + num2}, - Feita por Igor Gianeri Vieira")

        elif escolha == '2':  # Subtração
            num1 = float(input('Informe seu primeiro número: '))
            num2 = float(input('Informe seu segundo número: '))
            print(f"Resultado da Subtração: {num1 - num2}, Feita por Igor Gianeri Vieira")

        elif escolha == '3':  # Multiplicação
            num1 = float(input('Informe seu primeiro número: '))
            num2 = float(input('Informe seu segundo número: '))
            print(f"Resultado da Multiplicação: {num1 * num2}, Feita por Igor Gianeri Vieira")

        elif escolha == '4':  # Divisão
            num1 = float(input('Informe seu primeiro número: '))
            num2 = float(input('Informe seu segundo número: '))
            if num2 != 0:
                print(f"Resultado da Divisão: {num1 / num2}, Feita por Igor Gianeri Vieira")
            else:
                print("Erro! Divisão por zero.")

        elif escolha == '5':  # Potenciação
            base = float(input('Digite a base: '))
            expoente = float(input('Digite o expoente: '))
            print(f"Resultado da Potenciação: {math.pow(base, expoente)}, Feita por Igor Gianeri Vieira")

        elif escolha == '6':  # Raiz Quadrada
            num = float(input('Digite o número para calcular a raiz quadrada: '))
            if num >= 0:
                print(f"Resultado da Raiz Quadrada: {math.sqrt(num)}, Feita por Igor Gianeri Vieira")
            else:
                print("Erro! Não é possível calcular a raiz quadrada de um número negativo.")

        elif escolha == '7':  # Pi (π)
            print(f"Valor de Pi: {math.pi}, Feita por Igor Gianeri Vieira")

        elif escolha == '8':  # Tangente
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado da Tangente: {math.tan(radiano)}, Feita por Igor Gianeri Vieira")

        elif escolha == '9':  # Cosseno
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado do Cosseno: {math.cos(radiano)}, Feita por Igor Gianeri Vieira")

        elif escolha == '10':  # Seno
            angulo = float(input('Digite o ângulo em graus: '))
            radiano = math.radians(angulo)
            print(f"Resultado do Seno: {math.sin(radiano)}, Feita por Igor Gianeri Vieira")

        elif escolha == '11':  # Logaritmo
            num = float(input('Digite o número para calcular o logaritmo: '))
            if num > 0:
                print(f"Resultado do Logaritmo: {math.log(num)}, Feita por Igor Gianeri Vieira")
            else:
                print("Erro! O logaritmo de números negativos ou zero não é definido.")

        elif escolha == '12':  # Fatorial
            num = int(input('Digite um número inteiro para calcular o fatorial: '))
            if num < 0:
                print("Erro! O fatorial de um número negativo não é definido.")
            else:
                print(f"Resultado do Fatorial: {math.factorial(num)}, Feita por Igor Gianeri Vieira")

        elif escolha == '13':  # Sair
            print("Obrigado por usar a calculadora e boa volta!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    calc()
