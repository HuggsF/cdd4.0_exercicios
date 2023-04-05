alunos = int(input("Quantos alunos tem na turma?"))
soma_das_notas = 0
for x in range(alunos):
    nota_1 = int(input("Digite a primeira nota."))
    nota_2 = int(input("Digite a segunda nota."))
    soma_das_notas += nota_1+nota_2

print("A média da turma é: ", soma_das_notas/(alunos*2))

