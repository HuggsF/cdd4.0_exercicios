import strip
def texto_paraquantidade(texto):
    return len(texto.replace(" ", "")), texto[::-1]

print(texto_paraquantidade("      j       j        "))