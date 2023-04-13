numero_de_alunos = int(input("Quantos alunos a sala possui? "))
numero_divisor = numero_de_alunos
soma_das_notas = 0

while numero_de_alunos > 0:
    nota_do_aluno = float(input("Digite a nota do aluno: "))
    soma_das_notas += nota_do_aluno
    numero_de_alunos -= 1

print(soma_das_notas/numero_divisor)