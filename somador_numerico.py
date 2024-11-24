cont = 1
soma = 0
maior = 0 

while cont <= 2 :
    n = int(input("Informe um valor: "))
    if n > maior:
        maior = n
    soma += n
    cont += 1
print ("A soma de todos os valores foi ", soma)
print ("O maior numero é: ", maior)