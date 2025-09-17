import pandas as pd


def processar_logs_treinamento(File_name):
    try:
        df = pd.read_csv(File_name)
        media_tempo = df["tempo"].mean()
        desvio_padrao_tempo = df["tempo"].std()
        print(f"A média do tempo de execução: {media_tempo:.2f} segundos")
        print(f"Desvio padrão de tempo de execução: {desvio_padrao_tempo:.2f} segundos")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception:
        print(f"Erro ao processar o arquivo: {file_name}")

file_name = input("digite o nome do arquivo de log: ")
processar_logs_treinamento(file_name)