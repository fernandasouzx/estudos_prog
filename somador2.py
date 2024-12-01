soma = 0
qtd = int(input("Quantas vezes voce quer somar? "))

cont = 1
while cont <= qtd :
    num = int(input("Digite o valor: "))
    soma += num
    cont += 1
print("Soma = ", soma)