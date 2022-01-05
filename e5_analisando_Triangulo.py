"""Programa que lê o comprimento de 3 retas e
diz ao usuário se elas podem ou não formar um triângulo"""

print("Analisador de triângulo: ")
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos acima podem formar triângulo!")
else:
    print("Os segmentos acima não podem formar triângulo")
