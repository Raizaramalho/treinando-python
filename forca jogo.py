from msvcrt import kbhit
import random
from re import L
from tkinter import N

palavras = ["computador", "cachorro", "mulher", "brasil", "parede"]
palavra = random.choice(palavras)
print(palavra)

tentativas = 0 

chances = 8 

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)


print (" Bem vindo ao jogo da forca")
print (" Seu objetivo é tentar acertar a palavra secreta")
print (" Você terá que tentar uma letra por vez")
print (" Caso você acerte, a letra sera colocada na posição correta da palavra")
print (" caso você erre, você perderá uma chance, Você tem no máximo ", chances , "tentativas" )

while tentativas < chances and ''.join(estado_atual) != palavra:
 letra = input("\n\nqual letra você quer tentar? ")
 while letra in letras_escolhidas:
     print("você escolheu uma letra que já tinha sido escolhida, tente novame.nte")
 letra = input("\nqual letra você quer tentar? ")
 
 letras_escolhidas.append(letra)

if letra in palavra: 
 print("parabéns, você acertou a letra")
for item in range(len(palavra)):
 if letra == palavra[item]:
      estado_atual[item] = letra
else:
 print("que pena você errou!")
 tentativas = tentativas + 1
 
 #quantas tentativas ele tem 
 print("você ja fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )
 
 #qual o estado atual da palavra 
 print("esse é o estado atual:")
 print (estado_atual)
 
 #quais as letras ele ja tentou
 
 print("as letras que você ja tentou são:")
 print(letras_escolhidas)
for item in letras_escolhidas:
     print(item, end=" ")
 
 
#fazer um final para o jogo

if tentativas == chances:
 print("\n\nVocê perdeu! " )
 print("acabaram suas tentativas")
else:
    print("\n\nvc ganhou !")
    print("a palavra era",  palavra )