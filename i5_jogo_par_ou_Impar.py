"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

print("="*30)
print("Vamos jogar PAR ou ÍMPAR!")
print("="*30)

computador = randint(1, 5)
contador = 0

while True:
    jogador = int(input("Diga um valor: "))
    opcao = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    print("-"*30)
    resultado = jogador + computador
    if resultado % 2 == 0:
        print(f"Você jogou {jogador} e o computador {computador}. O total deu {resultado}: PAR")
        print("-"*30)
        if opcao in "P":
            print("Você venceu!")
            print("Vamos jogar novamente!")
            print("="*30)
            contador += 1
        else:
            print("Você perdeu!")
            print("=" * 30)
            break
    else:
        print(f"Você jogou {jogador} e o computador {computador}. O total deu {resultado}: ÍMPAR")
        print("-"*30)
        if opcao in "I":
            print("Você venceu!")
            print("Vamos jogar novamente!")
            print("="*30)
            contador += 1
        else:
            print("Você perdeu!")
            print("=" * 30)
            break
print(f"GAME OVER, você ganhou {contador} vezes.")
