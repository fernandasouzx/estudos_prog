cont = 1
qtd = int (input("Quantas vezes voce quer converter? "))

while cont <= qtd :
    
    r = float(input("Qual valor em R$ ? "))
    d = r/2.20
    print(f'O valor convertido e US$ {d:.2f}')
    cont += 1