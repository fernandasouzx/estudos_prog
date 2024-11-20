print("----------------------")
print("ESCOLA JAVALI CANSADO")
print("----------------------")

n1 = float (input("Nota 1: "))
n2 = float (input("Nota 2: "))

media = (n1 + n2)/2
print("----------------------")
print (f'MEDIA:  {media:.1f}') 

if (media >= 7):
    print ("ALUNO APROVADO")
    print("----------------------")
elif(media >= 5) and (media <7):
    print ("ALUNO EM RECUPERACAO")
    print("----------------------")
else:
    print ("ALUNO REPROVADO")
    print("----------------------")