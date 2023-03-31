user_1 = float(input("Digite o primeiro número de usuário"))
user_2 = float(input("Digite o segundo número de usuário"))
resposta = int(input("Os números de usuário são iguais? Responda 1 para SIM e 2 para NÃO."))


if user_1 == user_2:
    print("Os números sáo iguais" , user_1 , user_2)
else:
    if user_1 > user_2:
        print(user_1 , " , ", user_2)
    else:
        print(user_1 , " , ", user_2)
