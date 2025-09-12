"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
import os

while True:
    try:
        os.system("cls")
        print("selecione o modo de conversão:")
        print("\n1. Celsius --> Fahrenheit")
        print("2. Fahrenheit --> Kelvin")
        print("3. Kelvin --> Celsius")
        print("4. Fahrenheit --> Celsius")

        selecao = int(input("/> "))

        match selecao:
            case 1:
                # Celsius
                C = float(input("°C: "))
                # Calculo 
                F = (C * 1.8) + 32
                # Exibição
                print(f"{C}°C --> {F}°F")
                os.system("pause")
            case 2:
                # Fahrenheit
                F = float(input("°F: "))
                # Calculo
                K = (F + 459.67) * (5/9)
                print(f"{F}°F --> {K:.2f}°K")
                os.system("pause")
            case 3:
                # Kelvin
                K = float(input("°K: "))
                # Calculo
                C = (K - 273.15)
                print(f"{K}°K --> {C:.2f}°C")
                os.system("pause")
            case 4:
                # Fahrenheit
                F = float(input("°F: "))
                # Calculo
                C = (F - 32) * (5/9)
                print(f"{F}°F --> {C:.2f}°C")
                os.system("pause")
    
    except ValueError:
        print("Erro de inserção")
        os.system('pause')
        os.system("cls")
        continue
    except KeyboardInterrupt:
        print("saindo...")
        break


# Não coloquei mais opções de conversão porque isso já deve ser o bastante