import random
print ("BEM VINDO AO JOKENPO DA RAIZA")

print (" suas escolhas possiveis sao pedra, papel ou tesoura ")
escolha_nossa = input("qual sua escolha ?")
possibilidade = ["papel" , "tesoura", "pedra" ]
escolha_computador = random.choice(possibilidade)
print(escolha_computador )
  
  
if escolha_nossa == escolha_computador :
  print("empate") 
elif escolha_nossa == "pedra" and escolha_computador == "tesoura":
     print ("voce ganhou")
elif escolha_nossa == "pedra" and escolha_computador  == "papel":
    print ("voce ganhou")
elif escolha_nossa == "tesoura" and escolha_computador == "papel":
    print ("voce ganhou")
elif escolha_nossa == "tesoura" and escolha_computador  == "pedra":
    print ("voce perdeu")
elif escolha_nossa == "papel" and escolha_computador == "tesoura":
    print ("voce perdeu")
elif escolha_nossa == "papel" and escolha_computador == "pedra":
    print ("voce ganhou")
