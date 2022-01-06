"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro , ele não
será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.

lista = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor duplicado! Não vou adicionar...")
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if continuar in "N":
            break
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso...")
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
        if continuar in "N":
            break

print(f"Você digitou os valores {sorted(lista)}")
"""
numeros = list()

while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado: Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if r in "N":
        break
print("-"*30)
numeros.sort()
print(f"Você digitou os valores {numeros}")
