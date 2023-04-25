vetor = ["1","1","1","1","1","1","1","1","1","1","1","1"]

vetorCheck = input("Digite o número que deseja pesquisar.")
count = 0

for x in range(len(vetor)-1):
    if vetor[x] == vetorCheck:
        count += 1

print(f"{count}")