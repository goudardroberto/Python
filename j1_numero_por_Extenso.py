"""
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
 e mostrá-lo por extenso.

 # Forma 1
 numeros = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input("Entre com um número de UM a VINTE para obtê-lo por extenso: "))

while True:
    if numero < 1 or numero > 20:
        numero = int(input("Entre novamente com um número de 1 a 20: "))
    else:
        for i, extenso in enumerate(numeros):
            i = i + 1
            if i == numero:
                print(extenso)
        break

# Forma 2
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

sair = ''

while sair != 'N':
    while True:
        numero = int(input("Entre com um número de 0 a 20 para obtê-lo por extenso: "))
        if 0 <= numero <= 20:
            break
        print("Tente novamente: ", end='')
    print(f'Você digitou o número {numeros[numero]}')
    sair = input("Deseja continuar? [S/N]: ").strip().upper()[0]
"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
