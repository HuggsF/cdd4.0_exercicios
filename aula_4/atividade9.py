senha_correta = "gzy3v4q2"
tentativa = 3
senha = input("Digite sua senha: ")
while senha != senha_correta:
    tentativa -= 1
    if tentativa == 0:
        print("foi triste amigão, SENHA BLOQUEADA")
        exit()
    senha = input("Senha incorreta:")
print("Login feito com sucesso.")