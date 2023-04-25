login = []
senha = []

for x in range(5):
    dado1 = input("Cadastre um login.")
    login.append(dado1)
    dado2 = input("Cadastre uma senha.")
    senha.append(dado2)

print(f"{login} senha {senha}")

logincorreto = input("Digite seu login.")

if logincorreto in login:
    senhacorreta = input("Digite sua senha: ")
    if senhacorreta in senha:
        if logincorreto.index == senhacorreta.index:
            print(f"Login bem sucedido.")
        else:
            print(f"Senha Incorreta.")
else:
    print(f"Login não enconttrado no sistema.")