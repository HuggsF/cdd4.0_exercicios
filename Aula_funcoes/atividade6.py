def calcular_valor_total_estoque(nome,quantidade,valor_unitario):
    return quantidade*valor_unitario,nome

retorno = calcular_valor_total_estoque("Maça",60,2)

print(f'O produto {retorno[1]} está em seu estoque, totalizando {retorno[0]} em estoque.')