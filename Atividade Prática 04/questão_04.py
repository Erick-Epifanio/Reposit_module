def analisador_numerico():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        try:
            entrada = int(input("digite um numero inteiro ou Ctrl+C para parar o programa: "))
            if entrada % 2 == 0:
                print(f"{entrada} é um numero par")
                numeros_pares += 1

            else:
                print(f"{entrada} é um numero ímpar")
                numeros_impares += 1
        except ValueError:
            print("Erro -- Entrada invalidada")
            continue
        except KeyboardInterrupt:
            break
    
    print("\nResultado")
    print(f"Numeros ímpares: {numeros_impares}")
    print(f"numeros pares: {numeros_pares}")

analisador_numerico()