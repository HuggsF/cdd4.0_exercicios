def numerosprimos(*numeros):
    primos = []
    for x in numeros:
        if x % 2 != 0 and x % 3 != 0 and x != 1 and x % 5 != 0 and x % 11 != 0 or x == 2 or x == 3 or x == 5 or x == 11:
            primos.append(x)
    return primos

print(numerosprimos(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25))