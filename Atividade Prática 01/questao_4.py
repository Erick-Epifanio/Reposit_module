"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""
# Declaração das variaveis
nome_do_produto = str(input("Nome do produto: "))
Preco_unitario = float(input("Valor unitario do produto: "))
Quantidade = int(input("Quantidade: "))

# Valor total da quantidade de cadeiras
valor_total = Preco_unitario * Quantidade


# As 4 linhas abaixo é responsavel por exibir todos os dados armazenados no programa + o resultado
print(f"\nNome do produto: {nome_do_produto}")
print(f"Preço por unidade: R${Preco_unitario}")
print(f"Quantidade: {Quantidade}")
print(f"\nPreço total a ser pago: R${valor_total}\n")

# Questão concluida!
