"2 - Criar um código que registre as notas de alunos e calcular a média da turma."

import os
Dic_note = {}

def tratamento_dos_dados():
    Generic_name = "nota-"
    Indice = 0
    while True:
        
        try:
            while True:
                # preparando o nome de atribuição
                Indice += 1
                Fixed_name = Generic_name + f"{Indice}"
                
                # entrada de dados do usuário, caso ele apenas aperte Enter, o valor será atribuido para não truncar
                try:
                    insert = int(input(">")) or 1
                except ValueError:
                    insert = 1

                # Atribuindo de forma dinamica o dicionario
                Dic_note[Fixed_name] = insert
        except KeyboardInterrupt:
            break
    
    for Key, Dados in Dic_note.items():
        print(f"{Key} - {Dados}")
    

def media():
    filtro = []
    for item in Dic_note.values():
        filtro.append(item)
    soma = (sum(filtro)) / len(filtro)
    return f"Resultado {soma}"

tratamento_dos_dados()
print(media())