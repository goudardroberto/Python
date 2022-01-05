"""Mostre a tabuada de um número que o usuário escolher,
só que utilizando um laço for."""

# Forma complicada
# num = int(input("Entre com o número para ver sua tabuada: "))
# print("=" * 15)
# cont = 0
# for i in range(0, 11):
#     res = cont * num
#     print("{} x {} = {}".format(cont, num, res))
#     cont = cont + 1
# print("=" * 15)

# Forma simplificada
num = int(input("Entre com o número para ver sua tabuada: "))
print("=" * 15)
for i in range(0, 11):
    print("{} x {} = {}".format(i, num, num * i))
print("=" * 15)
