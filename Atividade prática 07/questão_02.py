import csv

def escrever_csv(nome_do_arquivo, dados):
    try:
        if ".csv" in nome_do_arquivo:
            with open(nome_do_arquivo, "w", newline='', encoding="utf-8") as file_csv:
                whiterfile = csv.writer(file_csv)
                whiterfile.writerow(["nome", "idade", "Cidade"])
                for item in dados:
                    whiterfile.writerow(item)
            print(f"Dados salvos no arquivo {nome_do_arquivo}")
        else:
            raise Exception()
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as type_error:
        print(f"Erro - {type_error}")


dados = [
    ["Erick","18","São Paulo"],
    ["Bryan", "18","São Paulo"],
    ["Vitor", "17", "São Paulo"]
]
file_name = input("Digite o nome do arquivo: ").strip()
escrever_csv(file_name, dados)