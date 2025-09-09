"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

# Variaveis dinamicas

Nota1 = float(input("Nota 1:"))
Nota2 = float(input("Nota 2:"))
Nota3 = float(input("Nota 3:"))

# Calculo

Soma = Nota1 + Nota2 + Nota3
Divisão = Soma/3

print(f"Nota 1: {Nota1}")
print(f"Nota 2: {Nota2}")
print(f"Nota 3: {Nota3}")
print(f"Média: {Divisão:.1f}")