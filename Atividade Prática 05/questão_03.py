import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    if "erro" in dados:
        print("CEP invalido ou não encontrado")
    else:
        print(f"Rua: {dados["logradouro"]}\nBairro: {dados["bairro"]}\nLocalidade: {dados["localidade"]}\nEstado: {dados["uf"]}")

cep = input("Digite o cep (tudo junto): ")

buscar_endereco(cep)