# Desafio
# Criar uma calculadora para realizar operações matemáticas básicas

# Requisitos
# 1. As operações matemáticas devem ser realizadas entre dois números
# 2. As operações básicas são: soma, subtração, multiplicação e divisão
# 3. O programa deve tratar entradas inválidas

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada (+,-*,/): ")
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida")
            print(f"O resultado da operação é {resultado}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}. Divisão por zero não permitido. Tente novamente.")
            
calculadora()