"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

# Declaração de valores + entrada de dados dinamica
Valor_real = float(input("Valor em real: "))
Taxa_dolar = 5.20
Taxa_euro = 6.15

# Variaveis auxilíares (para calcular os numeros)
Valor_convertido_dolar = Valor_real / Taxa_dolar
Valor_convertido_euro = Valor_real / Taxa_euro


# Exibição dos resultados
print(f"Valor em Real: R$ {Valor_real}")
print(f"Taxa do dolar: ${Taxa_dolar}")
print(f"Taxa do Euro: ${Taxa_euro}")
print(f"Valor convertido com Dolar: ${Valor_convertido_dolar:.2f}")
print(f"Valor convertido com Euro: ${Valor_convertido_euro:.2f}")