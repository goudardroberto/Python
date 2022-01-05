"""Programa que faz o computador "pensar" em um número inteiro entre 0 e 5 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
o programa deve escrever na tela se o jogador venceu ou perdeu"""


from random import randint
from time import sleep

print("-" * 10 + "Adivinhação" + "-" * 10)
numero = int(input("Vou pensar em um número de 0 a 5. Tente adivinhar:"))
computador = randint(0, 5)
print("PROCESSANDO...")
sleep(2)
if numero == computador:
    print("Você ganhou! Como sabia?")
else:
    print(f"Você perdeu! Eu pensei no número: {computador}!")
print("----Fim----")
