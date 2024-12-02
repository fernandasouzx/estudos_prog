# algoritmo "SeletorPessoas"
# =============================================================
# Algoritmo para ler Sexo, Idade e Cor de Cabelo de diversas pessoas e ao final, mostrar:
#     = Total de HOMENS com mais de 18 ANOS e cabelos CASTANHOS.
#     = Total de MULHERES entre 25 e 30 ANOS e cabelos LOIROS.

resp = "S"
totalH = 0
totalM = 0
while resp == "S":
    print("==========================")
    print("    SELETOR DE PESSOAS    ")
    print("==========================")

    sexo = str(input("Qual o Sexo? [M/F] "))

    idade = int(input("Qual a idade? "))

    print("Qual a cor do Cabelo?")
    print("[1] preto")
    print("[2] castanho")
    print("[3] ruivo")
    print("[4] loiro")
    corCabelo = int(input())

    # verfica as condicoes para calcular o Total de HOMENS com mais de 18 ANOS e cabelos CASTANHOS.
    if ((sexo == "M") and (idade > 18) and (corCabelo == 2)):
        totalH += 1

    # verfica e contabiliza o Total de MULHERES entre 25 e 30 ANOS e cabelos LOIROS.
    elif ((sexo == "F") and ((idade >= 25) and (idade <= 30)) and (corCabelo == 4)):
        totalM += 1
    resp = str(input("Quer continuar? [S/N] "))
    print("---------------------")

print("------------------------------------")
print(" RESULTADO FINAL ")
print("------------------------------------")
print("Total de homens com mais de 18 e cabelos castanhos ", totalH)
print("Total de mulheres entre 25 e 30 e cabelos loiros ", totalM)
