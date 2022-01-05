"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

# Usando a biblioteca math
# from math import factorial
# n = int(input("Digite um número para calcular o seu Fatorial: "))
# f = factorial(n)
# print("O fatorial de {} é {}".format(n, f))

# Fazendo de forma tradicional
n = int(input("Entre com um número para calcular o seu Fatorial: "))
c = n
# Para soma e subtração o fator nulo é zero, para a multiplicação o fator nulo é 1
f = 1

print(f"Calculando {n}! = ", end="")
while c > 0:
    print(f"{c} ", end="")
    print("x " if c > 1 else "= ", end="")
    f *= c
    c -= 1
print(f"{f}")
