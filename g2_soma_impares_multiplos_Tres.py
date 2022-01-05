""" Programa que calcula a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

# Acumulador
soma = 0
# Contador
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont = cont + 1 # ou cont += 1
        soma = soma + i # ou soma += i
print(f"A soma de todos os {cont} valores solicitados é {soma}.")
