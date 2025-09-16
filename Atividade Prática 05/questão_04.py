import datetime

def calcular_idade_dias(ano_de_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_de_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

print(f"sua idade em dia é aproximadamente : {calcular_idade_dias(ano_nascimento)} dias")