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

"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)."""

contador = num = s = 0

while True:
    num = int(input("Digite um valor [999 para parar: "))
    # Aqui ele não somará o 999 pois a condição esta antes da soma dos valores
    if num == 999:
        break
    s += num
    contador += 1
# O .format() está desatualizado
# print("A soma vale {}!".format(s))
# Utilizar a formatação de strings como está abaixo
print(f"Foram digitados {contador} e a soma vale {s}")

