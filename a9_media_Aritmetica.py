"""Programa que lê duas notas de um aluno, calcula e mostre a sua média."""

# Não esquecer a ordem de precedência dos valores -> (), **, *, /, //, %, +, -
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A nota {nota1} somada a nota {nota2} tem como média o valor: {media}")
