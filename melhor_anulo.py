print("------------------------")
print(" Escola Santa Paciencia ")
print("------------------------")

qtd_alunos = int(input("Quantos alunos a turma tem? "))


cont = 1
maiornota = 0.0

while cont <= qtd_alunos:

    print("---------------")
    print("ALUNO ", cont)

    nome = str(input("Nome do aluno: "))
    nota = float(input("Nota: "))

    if nota > maiornota:
        maiornota = nota
        melhoraluno = nome

    cont += 1

print("-------------------")
print("O melhor aproveitamento foi de ",
      melhoraluno, " com a nota ", maiornota)
