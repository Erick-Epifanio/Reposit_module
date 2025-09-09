"""
3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.

"""
# Recomendação para o uso correto
print("digite todos os valores em Cm")

# Declaração das variaveis necessarias para o calculo
Comprimento = float(input("Comprimento: "))
Largura = float(input("Largura: "))
Altura = float(input("Altura: "))

# Variavel responsavel por armazenar e valor produto do calculo.
volume = Comprimento * Largura *Altura

# As 4 linhas abaixo é responsavel por exibir todos os dados armazenados no programa + o resultado
print(f"\nComprimento: {Comprimento}")
print(f"Largura: {Largura}")
print(f"Altura: {Altura}\n")
print(f"Volume: {volume}Cm³\n")

# Questão concluida!
