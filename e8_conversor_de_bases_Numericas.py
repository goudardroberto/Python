"""Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário,
2 para octal e 3 para hexadecimal."""

num = int(input("Entre com um número inteiro qualquer: "))

print("\nTransforme para:")
print("[ 1 ] para binário")
print("[ 2 ] para octal")
print("[ 3 ] para hexadecimal")
escolha = int(input("\nEscolha uma opção: "))

# Todas essas saídas vão possuir prefixos.
# Exemplo: em binário o prefixo é: 0b
# Para tratar a saída, precisamos usar o conceito de fatiamento de strings,
# a primeira e segunda posição não queremos? então colocamos bin(num)[2:]

if escolha == 1:
    print(f"O número {num} em binário é: {bin(num)[2:]}")
elif escolha == 2:
    print(f"O número {num} em octal é: {oct(num)[2:]}")
elif escolha == 3:
    print(f"O número {num} em hexadecimal é: {hex(num)[2:]}")
else:
    print("Opção inválida!")
