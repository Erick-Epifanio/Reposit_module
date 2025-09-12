def verificar_senha():
    while True:

        senha = input("digite uma senha: ")

        if len(senha) < 8:
            print("por quetsões de segurança, refaça sua senha, pois não alcançou 8 ou mais digitos")
            continue

        if not any(letra.isdigit() for letra in senha):
            print("por quetsões de segurança, sua senha deve ter pelo menos um numero")
            continue

        print("Senha valida!")
        break

verificar_senha()