"""Programa que entra com um nome próprio,
apresenta o nome em letras maiúsculas,
apresenta o nome em letras minúsculas,
verifica o tamanho da string e
apresenta o primeiro nome e conta seu tamanho"""

nome = str(input("Entre com o seu nome: ")).strip()
print("Analisando seu nome: ")
print(f"Seu nome em maiúsculas é {nome.upper()}.")
print(f"Seu nome em minúsculas é {nome.lower()}.")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.")
# print(f"Seu primeiro nome tem {nome.find(' ')} letras.")
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.")
