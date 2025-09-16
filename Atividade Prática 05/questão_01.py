import random
import string

def gerador_de_senha(tamanho):
    letras = string.ascii_letters + string.digits + string.punctuation
    senha = " ".join(random.choice(letras) for _ in range(tamanho) )
    return senha

tamanho = int(input("digite o tamanho da senha: "))
senha_gerada = gerador_de_senha(tamanho)
print(f"Sua senha é: {senha_gerada}")