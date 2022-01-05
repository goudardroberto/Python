"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo."""

while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    if num < 0:
        break
    print("=" * 20)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("=" * 20)
print("Programa tabuada encerrado!")
