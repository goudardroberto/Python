""" Programa que lê o nome completo de uma pessoa
mostrando em seguida o primeiro e último nome separadamente"""

n = str(input("Digite o seu nome: ")).strip()
nome = n.split()
print(f"O seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome) - 1]}")
