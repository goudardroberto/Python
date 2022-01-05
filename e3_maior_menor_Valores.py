""" Programa que recebe 3 números e identifique o maior e menor"""

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

# Verificando menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando maior valor
maior = c
if b > c and b > a:
    maior = b
if a > c and a > b:
    maior = a
print(f"O maior valor é {maior} e o menor valor é {menor}.")
