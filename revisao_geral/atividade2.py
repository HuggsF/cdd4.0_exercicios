numeros = []
for x in range(3):
    numeros.append(int(input('Input your numbers: ')))

print(f'{max(numeros)}')

max_number = 0
for numero in range(len(numeros)):
    if max_number < numeros[numero]:
        max_number = numeros[numero]
print(f'{max_number}')


