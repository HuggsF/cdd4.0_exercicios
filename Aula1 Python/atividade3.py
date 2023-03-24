nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
aumento = float(input("Digite a % de aumento anual de salário: "))
salario_final = float(salario+salario*(aumento/100))


print("Nome: ", nome, "\n Idade: ", idade, "\n Salário: ", salario)

print("Ano que vem o seu salário vai estar", aumento, "% mais alto, totalizando: ", salario_final)

