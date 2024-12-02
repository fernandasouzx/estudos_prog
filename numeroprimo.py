#numero primo é divisivel por 1 ou ele mesmo

number = int(input("Informe um valor: "))
contador = 1
contdiv = 0

while (contador <= number) :
    if (number % contador == 0):
        contdiv += 1
    contador += 1
    
if(contdiv > 2):
    print("O valor ", number, "nao e primo.")
else:
    print("O valor ", number, " e primo.")