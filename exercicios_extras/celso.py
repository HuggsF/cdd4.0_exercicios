aux = 0
a = 0
b = 1
for i in range(5):
    aux = a + b
    a = b
    b = aux
print(f'{aux}{a}{b}')
    