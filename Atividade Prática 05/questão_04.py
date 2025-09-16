import requests

def buscar_cotacao(moedas):
    url = f'https://economia.awesomeapi.com.br/json/last/{moedas}-BRL'
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    chave = moedas + "BRL"

    if chave not in dados:
        print("Moeda não encontrada")
        return
    
    info = dados[chave]

    print(f"Cotação:{moedas}/BRL\nValor Atual: {info["bid"]}\nValor maximo: {'high'}\nValor minimo: {info["low"]}\nUltima Atualização: {info["create_date"]}")


moedas = input("Digite um codigo de moeda (Ex: USD, EUR, GBP): ").upper()

buscar_cotacao(moedas)