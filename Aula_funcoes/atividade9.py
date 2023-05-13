def filtrar_elementos_repetidos(lista):
    nova_lista = []
    nova_lista.extend(set(lista))
    return nova_lista

print(filtrar_elementos_repetidos([1,1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7]))

def filtrar_elementos_rep(lista):
    lista2=[]
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    return lista2

print(filtrar_elementos_repetidos([1,1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7]))
