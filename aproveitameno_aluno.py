n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2)/2


if (media >= 9) and (media <= 10):
    aproveitamento = "A"

elif (media >= 8) and (media < 9):
    aproveitamento = "B"

elif (media >= 7) and (media < 8):
     aproveitamento = "C"

elif (media >= 6) and (media < 7):
    aproveitamento = "D"

elif (media >= 5) and (media < 6):
     aproveitamento = "E"
    
else :
     aproveitamento = "F"
     
print(f'MEDIA: {media:.2f}')
print(f"APROVEITAMENTO: {aproveitamento}")