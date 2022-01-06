"""
Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivoas posições na lista.
"""
menor = 0
maior = 0

lista = []
for p in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {p}: ")))
    if p == 0:
        maior = menor = lista[p]
    else:
        if lista[p] > maior:
            maior = lista[p]
        if lista[p] < menor:
            menor = lista[p]

print("- "*30)
print(f"Você digitou os valores: {lista}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
print()
