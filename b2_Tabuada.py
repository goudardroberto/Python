""" Programa que lê um número Inteiro qualquer e mostra na tela a sua tabuada."""

print("-" * 6 + "Tabuada" + "-" * 6)
num = int(input("Digite um número: "))
multiplicador = 0
resultado = 0
cont = 0

while cont < 11:
    print(f"{num} x {multiplicador} = {resultado}.")
    cont = cont + 1
    multiplicador = multiplicador + 1
    resultado = num * multiplicador
    continue

print("-" * 19)
