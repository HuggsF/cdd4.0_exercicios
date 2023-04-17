#number = int(input("Digite um número."))
#contador = 1
#while contador <= number:
#    i = 0
#    while i < contador:
#        print(contador)
#        i +=1
#    contador+=1

x = int(input("Digite"))
for x in range(1, x+1):
    for y in range(x):
        print(y, end=" ")
    print()