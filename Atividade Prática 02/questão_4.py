"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Variaveis
Distancia_percorrida = float(input("Distância percorrida (Km): "))
Combustivel_consumido = float(input("Combustível gasto (L): "))

# Calculo

Consumo_medio = Distancia_percorrida / Combustivel_consumido

#exibição

print(f"Distância percorrida: {Distancia_percorrida} km")
print(f"Combustível gasto: {Combustivel_consumido} litros")
print(f"Consumo médio: {Consumo_medio:.2f} km/l")