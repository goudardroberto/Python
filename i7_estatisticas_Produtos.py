"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

total = totmil = menor = cont = 0
barato = " "

while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$ "))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^30}".format("Fim do Programa"))
print(f"O total da compra foi {total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$ 1000")
print(f"O produto mais barato foi: {barato}, custando R${menor:.2f}")