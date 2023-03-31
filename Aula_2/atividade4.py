
combustivel = input("Qual o seu combustível?\n E - Etanol\n G - Gasolina\n").upper()
litros = float(input("Quantos litros de gasolina você deseja?"))
etanol = litros * 4.9
gasolina = litros * 5.8

if combustivel == "E":
    print("Você deverá pagar:", etanol)
elif combustivel == "G":
    print("Você deverá pagar:", gasolina)
else:
    print("Digite um tipo de combustível válido.")