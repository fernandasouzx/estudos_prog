
nome = str(input("Nome do Funcionario: "))
salario = float(input("Salario: "))
dependentes = int(input("Quantidade de dependentes: "))

if (dependentes == 0):
    salarioN = salario + (salario*5/100)


elif dependentes in [1, 2, 3]: #verifica se os valores estao na lista
    salarioN = salario + (salario*10/100)


elif dependentes in [4,5,6]: #verifica se os valores estao na lista
    salarioN = salario + (salario*15/100)

else:
    salarioN = salario + (salario*18/100)

print(f'Novo salario: R$ {salarioN:.2f}')
