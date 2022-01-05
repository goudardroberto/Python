"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

print("Sou seu computador...\nAcabei de pensar em número de 0 a 10.\nSerá que você consegue adivinhar qual foi?")
computador = randint(1, 10)
acertou = False
palpites = 0

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print("Mais... Tente mais uma vez!")
            palpites += 1
        else:
            print("Menos... Tente mais uma vez!")
            palpites += 1
print(f"Acertou com {palpites} tentativas. Parabéns!")
