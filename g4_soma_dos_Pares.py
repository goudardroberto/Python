"""Programa que lê seis números inteiros e
mostra a soma apenas dos pares.
Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i} número: ")
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"São {cont} números pares e a soma dos números pares é {soma}")
