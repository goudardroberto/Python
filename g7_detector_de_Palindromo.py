"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA; A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO; ANOTARAM A DATA DA MARATONA."""

# Eliminamos espaços antes e depois com o strip, passamos tudo para maiúscula
frase = str(input("Digite uma frase: ")).strip().upper()
# Separamos a frase em palavras com split numa lista
palavras = frase.split()
# Juntamos todas as palavras com join
junto = "".join(palavras)
inverso = ""

# len nos ajuda a ir da ultima letra, até a primeira, voltando uma letra (-1)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
# Esse for acima é o mesmo que ___ inverso = junto[::-1] ___ utilizando fatiamento

print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print(f"{junto} é um PALINDROMO")
else:
    print(f"{frase} não é um PALINDROMO")
