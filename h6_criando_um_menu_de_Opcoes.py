"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

controle = 0
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

while controle == 0:
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    opcao = int(input(">>>> Escolha uma opção: "))
    if opcao == 1:
        resultado = n1 + n2
        print("-" * 20)
        print(f"A soma {n1} + {n2} = {resultado}")
        print("-" * 20)
    elif opcao == 2:
        resultado = n1 * n2
        print("-" * 20)
        print(f"A multiplicação de {n1} x {n2} = {resultado}")
        print("-" * 20)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print("-" * 20)
            print(f"O maior número entre {n1} e {n2} é: {maior}")
            print("-" * 20)
        elif n1 < n2:
            menor = n2
            print("-" * 20)
            print(f"O maior número entre {n1} e {n2} é: {menor}")
            print("-" * 20)
        else:
            print("-" * 20)
            print(f"Os valores {n1} e {n2} são iguais")
            print("-" * 20)
    elif opcao == 4:
        print("-" * 20)
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print("-" * 20)
    elif opcao == 5:
        controle = 1
    else:
        print("Opção inválida!")
    sleep(2)
print("Fim do programa!")
