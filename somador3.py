soma = 0
resposta = "S"


while resposta == "S":
    num = int(input("Digite o valor: "))
    soma += num
    resposta = str(input("Quer continuar? [S/N] "))
print("Soma = ", soma)