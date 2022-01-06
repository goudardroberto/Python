"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    else:
        impares.append(valor)
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break

print("- "*30)
print(f"A lista completa é: {lista}")
print(f"A lista dos pares é: {pares}")
print(f"A lista dos ímpares é: {impares}")
"""
lista = []
pares = []
impares = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
for i, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)

    elif valor % 2 == 1:
        impares.append(valor)

print("- "*30)
print(f"A lista completa é: {lista}")
print(f"A lista dos pares é: {pares}")
print(f"A lista dos ímpares é: {impares}")
