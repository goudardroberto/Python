"""Algoritmo que recebe um número real e mostra sua porção inteira"""

from math import trunc

num = float(input("Entre com um número real: "))
print(f"O número digitado foi {num} e sua porção inteira é: {trunc(num)}")
