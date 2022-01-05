"""Programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar."""

# Jeito fácil

# real = float(input("Quanto dinheiro você tem na carteira? R$ "))
# dolar = real / 5.79
# print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real, dolar))

# Jeito difícil - Declarando funções

print("-" * 4 + "Conversor de Moedas" + "-" * 4)
print("Escolha o país destino da conversão: ")
print("Opção 1 = EUA;\nOpção 2 = China;\nOpção 3 - Canadá;\nOpção 4 - Japão.\n")
op = int(input("Digite a opção desejada: "))
real = int(input("Digite o valor em reais que queira converter: "))


def eua(real):
    valor = real * 0.1845
    return valor


def china(real):
    valor = real * 1.1901
    return valor


def canada(real):
    valor = real * 0.2319
    return valor


def japao(real):
    valor = real * 20.4666
    return valor


if op == 1:
    resultado = eua(real)
    print("Com R$ {} reais, você compra $ {} dólares.".format(real, resultado))
elif op == 2:
    resultado = china(real)
    print("$ ", resultado)
elif op == 3:
    resultado = canada(real)
    print("$ ", resultado)
elif op == 4:
    resultado = japao(real)
    print("$ ", resultado)
else:
    print("Opção errada!")

print("-" * 27)
