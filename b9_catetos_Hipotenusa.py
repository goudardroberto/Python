"""Programa que recebe o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo,
calcula e mostra o comprimento da hipotenusa."""

# Usando fórmulas
# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("Comprimento do cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f"A hipotenusa vai medir: {hi:.2f}")

# Usando a biblioteca math
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"A hipotenusa vai medir: {hi:.2f}")
