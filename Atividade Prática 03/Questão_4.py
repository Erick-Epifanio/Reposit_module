"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

anos = int(input("Determine quantos dias tem no ano: "))

if anos % 4 == 0 and anos % 100 != 0:
    print(f"{anos} é um ano bissexto.")
elif anos % 400 == 0:
    print(f"{anos} é um ano bissexto.")
else:
    print(f"{anos} não é um ano bissexto.")

    #não consegui resolver, não entendi o enunciado