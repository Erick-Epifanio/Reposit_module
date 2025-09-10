"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: 'classificacao = "Abaixo do peso"'
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""
# import a biblioteca
import os

# Loop do programa principal
while True:

    # Tenta executar
    try:
        # Entrada de dados do usuário
        peso = float(input("Kg: "))
        altura = float(input("Altura (em metros): "))
        IMC = peso / (altura**2)
        print(f"IMC = {IMC:.2f}")

        # Classifica o IMC
        if IMC < 18.5:
                print('classificação = Abaixo do peso')
        elif 18.5 <= IMC < 25:
                print('classificacao = Peso normal')
        elif 25 <= IMC < 30:
            print("classificacao = Sobrepeso")
        elif IMC > 30:
            print("classificacao = Sobrepeso")
    
    # Tratamentos de Erros
    except ValueError:
        print("Valor invalido")
        os.system("cls")
        continue    
    except KeyboardInterrupt:
        print("\nSaindo...")
        break