#postos_de_gasolina = [2, 15, 22, 10.2]
#combustivel = 16
#consumo = 2

def atividade_extra(postos_de_gasolina,combustivel,consumo):
  def postos_disponiveis(x):
    if x <= (combustivel*consumo):
      return True
    else:
      return False

  postos_de_gasolina = list(filter(postos_disponiveis, postos_de_gasolina))
  return max(postos_de_gasolina)

print(atividade_extra([2, 15, 22, 10.2],16,2))

count = 2


#while combustivel > 0:
#  postos_de_gasolina = list(filter(postos_disponiveis, postos_de_gasolina))
#  print(max(postos_de_gasolina))
#  count-=1
#  if count == 0:
#    print(max(postos_de_gasolina))
#    combustivel-=1
#    count = 2
