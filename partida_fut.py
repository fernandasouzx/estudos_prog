print("-------------------")
print("BANGU x MADUREIRA")
print("-------------------")

golsBangu = int (input("Quantos gols do BANGU? "))
golsMadureira = int (input("Quantos gols do MADUREIRA? "))



if ( golsBangu > golsMadureira):
    diferenca = golsBangu - golsMadureira
else:
    diferenca = golsMadureira - golsBangu
    
print("-------------------")
print( "DIFERENÇA: ", diferenca)

if diferenca == 0:
    print("STATUS: EMPATE")
    
elif diferenca in [1,2,3] :
     print("STATUS: PARTIDA NORMAL")

elif diferenca in [4,5,6]:
    print("STATUS: GOLEADA")

else:
    print("STATUS: ALGO INCOMUM")
    print("Voce digitou os dados corretos? ")

print("-------------------")