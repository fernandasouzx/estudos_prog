contador = 1

numero = int(input("Infome o valor da tabuada: "))

print ("\nTABUADA", numero, "\n")

for i in range(10):
    
    resultado = numero*contador
    print(numero, " X ", contador," = ", resultado)
    contador += 1
    