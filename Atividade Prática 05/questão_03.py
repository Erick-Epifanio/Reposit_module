"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""
import os

def calculo_geral(preco_inicial, porcentagem):
    desconto = (porcentagem/100)
    valor_do_desconto = preco_inicial * desconto
    preco_final = preco_inicial - valor_do_desconto
    return f"{porcentagem}% no preço inicial é igual a {valor_do_desconto} ---- O preço final é {preco_final}"

while True:
    try:
        preco_init = int(input("Digite o preco inicial: "))
        desconto = int(input("Digite o desconto: "))

        if preco_init <= 0:
            raise ValueError()
        if desconto <= 0:
            raise ValueError()
        else:
            break
    except ValueError:   
        print("Entrada de dados invalido")
        os.system("pause")
        continue

print(calculo_geral(preco_init, desconto))