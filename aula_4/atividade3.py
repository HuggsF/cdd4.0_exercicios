count = 0
for x in range(11):
    n = int(input("digite um numero: "))
    if n < 0:
        count+=1
print("você digitou ",count," numero(s) negativos.")
