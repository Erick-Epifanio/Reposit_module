import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, "r", newline= '', encoding="utf-8") as csv_file:
            leitor = csv.reader(csv_file)
            for linha in leitor:
                print(linha)
    except FileNotFoundError as erro:
        print(f"Erro - {erro}")        

file_name = input("digite o nome do arquivo: ").strip()
if ".csv" in file_name:
    ler_csv(file_name)
else:
    print("Arquivo invalido - é necessario que o arquivo tenha a extensão .csv")