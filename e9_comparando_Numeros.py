"""Escreva um programa que leia dois números inteiros e
compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

num1 = int(input("Entre com o primeiro valor: "))
num2 = int(input("Entre com o segundo valor: "))

if num1 > num2:
    print(f"O primeiro valor: {num1} é maior que o segundo valor: {num2}.")
elif num2 > num1:
    print(f"O segundo valor: {num2} é maior que o primeiro valor: {num1}.")
else:
    print("Os valores são iguais!")
