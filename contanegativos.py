cout = 1
totalN = 0

for i in range(5):

    number = int(input("Digite um numero: "))
    cout += 1

    if number < 0:
        totalN += 1
print ("Total de valores negativos digitados: ", totalN)