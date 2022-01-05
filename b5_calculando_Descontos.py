""" Algoritmo que receba o preço de um produto e mostra seu novo preço com 5% de desconto."""

# Fórmula: 10*5/100 significa cinco por cento de dez

# print("Calcule o preço de um produto com desconto de 5%: ")
# var1 = float(input("Entre com o valor do produto: "))
# res = var1 * 5 / 100
# res2 = var1 - res
# print("O produto com valor de R${} com desconto de 5%: (R${}) custará: R${}.".format(var1, res, res2))

# Utilizando uma linha

# preco = float(input("Qual é o preço do produto? "))
# novo = preco - (preco * 5 / 100)
# print(f"O produto que custava R${preco} com desconto de 5% vai custar R${novo}.")

# Algoritmo que receba o salário de um funcionário e calcule um aumento de 15%

salario = float(input("Digite aqui o salário do funcionário: "))
novo = salario + (salario * 15 / 100)
print(f"O salário com valor de R${salario} com aumento de 15% passará para R$: {novo}")
