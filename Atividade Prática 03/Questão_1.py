"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

import os
print("para fechar o programa pressione (Ctrl + C)")

# loop do programa
while True:

    try: # tenta exetucar o codigo

        idade = int(input("Digite sua idade: "))
        
        # verifica se a variavel idade é valido com as operações logicas abaixo
        if  idade >= 0 and idade <= 12:
            print("Criança")
        elif idade >= 13 and idade <= 17:
            print("Adolecente")
        elif idade >= 18 and idade <= 59:
            print("Adulto")
        elif idade >= 60:
            print("Idoso")

    # caso haja um erro, aqui o programa vai tentar entender o que é, e executar os blocos abaixo
    except ValueError:
        print(f"Erro -- Valor invalido")
        os.system("pause")
        os.system("cls")
        continue
    except KeyboardInterrupt:
        print("Saindo...")
        break
    
