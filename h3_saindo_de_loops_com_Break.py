"""
Saindo de loops com break

OBS: Em alguns programas, para a ferramenta funcionar utilizamos o looping infinito

Podemos utilizar o break para sair do looping de maneira projetada

# Exemplo 1

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")


# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ").strip().upper()[0]
    if comando == "S":
        break
"""
