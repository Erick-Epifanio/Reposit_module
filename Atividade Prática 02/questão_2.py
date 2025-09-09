"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

# Variaveis de entrada

Produto = str(input("Nome do produto: "))
Preco_original = float(input("Valor do produto: "))
Porcentagem_desconto = int(input("Valor do desconto: "))

# Variaveis de calculo

Conversao_decimal = Porcentagem_desconto / 100
Valor_do_desconto = Preco_original * Conversao_decimal
Valor_final = Preco_original - Valor_do_desconto

# Exibição

print(f"Nome do produto: {Produto}")
print(f"Preço original: R${Preco_original}")
print(f"Desconto: {Porcentagem_desconto}%\n")
print(f"Valor a ser descontado: R$-{Valor_do_desconto}")
print(f"Valor final a ser pago: R${Valor_final}")
