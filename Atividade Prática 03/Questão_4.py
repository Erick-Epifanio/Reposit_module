"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

import os
while True:
    try:
        ano = int(input("Determine quantos dias tem no ano: "))

        if (ano % 4 == 0) and (ano % 100 != 0):
            print(f"{ano} é um ano bissexto")
        elif ano % 400 == 0:
            print(f"{ano} é um ano bissexto")
        else:
            print(f"{ano} não é um ano bissexto")

        os.system("pause")
        os.system("cls")
    except KeyboardInterrupt:
        print("saindo....")
        break   
        

# Feito acompanhando o professor