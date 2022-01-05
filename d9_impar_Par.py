""" Programa que verifica se o número inserido é par ou ímpar"""

num = int(input("Entre com um número qualquer: "))
resto = num % 2

if resto == 0:
    print("Este número é par!")
else:
    print("Este número é ímpar!")
