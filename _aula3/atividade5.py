soma = 0
for x in range(10):
    y = int(input("Digita um numero ae, na vdd são 10."))
    if y % 2 != 0:
        soma += y
    else: continue

print("sua soma total é: ", soma)