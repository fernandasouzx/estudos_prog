#ALGORITMO QUE VERIFICA SE ESTA APTO A DIRIGIR
print("------- DEPARTAMENTO DE TRANSITO -------")

ano_atual = int(input("Ano atual (yyyy): "))
ano_nascimento = int(input("Ano de seu nascimento (yyyy): "))

idade = ano_atual - ano_nascimento
print("Idade: ", idade, " anos.")

if (idade >= 18):
    print ("Esta apto a dirigir!")
else:
    print ("Nao esta apto a dirigir.")