"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
menor = 0
maior = 0

for i in range(1, 8):
    nascimento = int(input(f"Em que ano a {i} pessoa nasceu? "))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo temos {maior} pessoas maiores de idade")
print(f"E também {menor} pessoas menores de idade")
