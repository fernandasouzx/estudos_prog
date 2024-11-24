
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))


print("--------------------")
print("  C O N T A N D O   ")
print("--------------------")

if fim > inicio:
    cont = inicio
    while cont <= fim:
        print(cont, "...")
        cont += 1

else:
    cont = inicio

    while cont >= fim:
        cont -= 1
        print(cont, "...")
