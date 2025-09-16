import requests


def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()


    user = dados["results"][0]
    nome = user["name"]["first"] + " " + user["name"]["last"]
    email = user["email"]
    country = user["location"]["country"]

    print(f"User: {nome}\nEmail: {email}\nCountry: {country}")

obter_usuario_aleatorio()