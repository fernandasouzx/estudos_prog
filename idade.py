#CALCULO IDADE
ano = int(input ("Em que ano estamos: "));
nascimento = int(input ("Ano em que voce nasceu: "));

#calculo de idade
idade = (ano - nascimento); 
print ("Em ", ano, " voce tera ", idade, " anos.");

if idade >= 21:
    print (" e ja tera alcançado a maioridade.");
    