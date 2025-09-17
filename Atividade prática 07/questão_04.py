import json

def ler_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file_json:
            dados = json.load(file_json)
            print(json.dumps(dados, indent= 4))
    except FileNotFoundError as erro:
        print(f"Erro -- {erro}")

def escrever_json(file_name, dados):
    try:
        with open(file_name, "w", newline='',encoding="utf-8") as file_json:
            json.dump(dados, file_json ,ensure_ascii= False, indent= 4)
    
    except ValueError as value:
        print(f"erro -- {value}")
    except FileNotFoundError as file_err:
        print(f"erro -- {file_err}")
    except TypeError as typererr:
        print(typererr)
        
dado = {
    "erick":"Desocupado",
    "Bryan":"furry????",
    "Vitor":"Autista"
}

file_name = input("Digite o nome do arquivo: ").strip()

if ".json" in file_name:
    select = int(input("escrever[0] ou ler[1]: ").strip())
    if select == 1:
        ler_json(file_name)
    elif select == 0:
        escrever_json(file_name, dado)
    else:
        print("seleção invalida")