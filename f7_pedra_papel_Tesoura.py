""" Programa que faz o computador jogar Jokenpô com você."""

from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")

print("=" * 40)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("=" * 40)
if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Você Venceu!")
    elif jogador == 2:
        print("Você Perdeu!")
    else:
        print("Opção inválida!")
elif computador == 1:
    if jogador == 0:
        print("Você Perdeu!")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Você Venceu!")
    else:
        print("Opção inválida!")
elif computador == 2:
    if jogador == 0:
        print("Você Venceu!")
    elif jogador == 1:
        print("Você Perdeu!")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Opção inválida!")