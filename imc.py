massa = float(input ("Massa (KG): "))
altura = float(input ("Altura (m): "))

imc = massa / (altura*altura)

print(f'IMC:  {imc:.2f}')
      
if (imc < 17 ):
    print ("Muito abaixo do peso")

elif(imc >= 17) and (imc <= 18.5):
    print("Abaixo do peso.")
    
elif(imc >= 18.5 ) and (imc < 25):
    print("Peso Ideal.")

elif(imc >= 25 ) and (imc < 30):
    print("Sobrepeso.")
    
elif(imc >= 30) and (imc < 35):
    print ("Obesidade")
    
elif(imc >= 35) and (imc < 40):
    print ("Obesidade Severa")
    
else:
    print ("Obesidade Morbida")
