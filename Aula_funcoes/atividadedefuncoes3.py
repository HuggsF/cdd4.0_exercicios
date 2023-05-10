def conta_vogais(str):
    vogais = "aeiou"
    count = 0
    for x in str.lower():
        if x in vogais:
            count+=1
    return count

print(f'{conta_vogais("O rato roeu a roupa do rei de roma.")}')