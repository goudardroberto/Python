"""Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50."""

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("Acabou!")

# Nesse caso ele gerou várias repetições que ocuparam a memória do computador
for i in range(1, 51):
    print(".", end="")
    if i % 2 == 0:
        print(i, end=" ")
print("Acabou!")

# Para contornar isso, podemos fazer de outro jeito, aqui o trabalho é feito pela metade
for i in range(2, 51, 2):
    print(".", end="")
    print(i, end=" ")
print("Acabou!")
