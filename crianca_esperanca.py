print("----------------------")
print("CRIANCA ESPERANCA")
print("----------------------")


print("Muito obrigada por ajudar!")

#exibir opcoes
print("[1] para doar R$ 10 ")
print("[2] para doar R$ 25 ")
print("[3] para doar R$ 50 ")
print("[4] para doar outros valores ")
print("[5] para cancelar")

#escolhaa do user

escolha = int (input("Escolha uma opcao: "))

#processamento de escolha
if (escolha == 1):
    valor = 10
    
elif (escolha == 2):
    valor = 25

elif (escolha == 3):
    valor = 50
    
elif (escolha == 4):
    valor = float(input("Digite o valor que deseja doar: R$ "))
    
elif(escolha == 5):
    valor = 0
    print("Voce cancelou a doacao. Obrigada por participar!")

else:
    valor = 0
    print("Opcao invalida!")
    

# exibir mensagem de confirmação, se aplicável
if (valor > 0):
    print("----------------------") 
    print(f'SUA DOACAO FOI DE R$ {valor:.2f}')
    print("----------------------")