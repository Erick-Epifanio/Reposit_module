def calcular_gorjeta(valor_da_conta, porcentagem_gorjeta):
    gorjeta = valor_da_conta * (porcentagem_gorjeta/100)
    return gorjeta

total_conta = int(input("digite o total da conta: "))
porcentagem = int(input("Quantos porcentos de gorjeta deseja pagar?: "))

gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta}, você deseja pagar {porcentagem}% ---- R${gorjeta} de gorjeta")
