"""Programa que lê uma frase e:
Conte quantas vezes aparece a letra "a",
em que posição ela aparece a primeira vez,
em que posição ela aparece a última vez,
quando for buscar alguma str,
lembrar de passar pra maiúscula antes
(rfind é pra procurar do lado direito para o esquerdo)
O + 1 é para ao apresentar, tirar a diferença do índice 0"""


frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra 'a' aparece {frase.count('A')} vezes")
print(f"A letra 'a' aparece na primeira posição em {frase.find('A') + 1}")
print(f"A letra 'a' aparece na última posição em {frase.rfind('A') + 1}")
