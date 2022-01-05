"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

print("Analisador de triângulo: ")
l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos podem formar triângulo:")
    # Python aceita l1 == l2 == l3, nesse caso automaticamente o l3 é igual ao l1
    if l1 == l2 and l2 == l3:
        print("EQUILÁTERO, com todos os lados iguais.")
    # Na forma reduzida, quando for diferença, l1 != l2 != l3 != l1
    # precisaremos identificar que o l3 é diferente do l1!
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print("ESCALENO, com todos os lados diferentes")
    # Podemos fazer com else no elif abaixo
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("ISÓSCELES, com dois lados iguais")
else:
    print("Os segmentos acima não podem formar triângulo")
