pares = []
impares = []
positivos = []
negativos = []
zeros = []
for x in range (10):
    numero = int(input('Um numero: '))
    if numero == 0:
        zeros.append(numero)
    elif numero %2 == 0 and numero > 0:
        pares.append(numero)
        positivos.append(numero)
    elif numero %2 == 0 and numero < 0:
        pares.append(numero)
        negativos.append(numero)
    elif numero % 2 != 0 and numero != 0 and numero > 0:
        impares.append(numero)
        positivos.append(numero)
    elif numero % 2 != 0 and numero != 0 and numero < 0:
        impares.append(numero)
        negativos.append(numero)
print(f'{pares}{impares}{positivos}{negativos}{zeros}')