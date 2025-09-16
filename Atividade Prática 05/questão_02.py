"""

while True:
    try:
        def conparacao():
            palavra = input("Digite a palavra: ").lower
            if palavra == palavra[::-1]:
                return "sim"
            else:
                return "não"
        print(conparacao())
    except KeyboardInterrupt:
        break
    
"""

def palindromo(texto):
    texto_limpo = " ".join(letra.lower() for letra in texto if letra.isalnum())
    
    return texto_limpo == texto_limpo[::-1]

frase = str(input("digite a frase: "))

resultado = palindromo(frase)

if resultado == True:
    resposta = "sim"
else:
    resposta = "não"
    
print(f"{frase} é um palíndromo? {resposta}")