"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""
import os


def calculadora():
    while True:
        try:
            Num1 = float(input("numero 1: "))
            Num2 = float(input("numero 2: "))
            operacao = str(input("(+,-,/,*): "))

            match operacao:
                case "+":
                    valor = Num1 + Num2
                    return f"{Num1} + {Num2} = {valor}"
                case "-":
                    valor = Num1 - Num2
                    return f"{Num1} - {Num2} = {valor}"
                case "/":
                    valor = Num1 / Num2
                    return f"{Num1} / {Num2} = {valor}"
                case "*":
                    valor = Num1 * Num2
                    return f"{Num1} * {Num2} = {valor}"
                case _:
                    raise ValueError()
        except ValueError:
            continue
        except ZeroDivisionError:
            print(f"não é possivel realizar divisão de zero")
            os.system("pause")
            os.system("cls")
            continue

print(calculadora())