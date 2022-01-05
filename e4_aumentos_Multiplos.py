"""Programa que recebe o salário de um funcionário e calcula o valor do seu aumento
para salários superiores a R$ 1.250,00, calcule um aumento de 10% e
para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input("Qual é o salário do funcionário? "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.")
