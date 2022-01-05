"""Programa que solicita valor da casa, valor do salario,
anos que deseja o financiamento e apresenta resposta com todos
os dados positiva se o valor nao ultrapassar 30% do salario,
negativa se for ao contrario."""

valor_Casa = float(input("Qual o valor da casa desejada?: "))
valor_Salario = float(input("Qual o valor do seu salário?: "))
total_Anos = int(input("Qual o total de anos para o financiamento?: "))

meses = total_Anos * 12
parcela = valor_Casa / meses
pagamento = valor_Salario * (30 / 100)

if parcela < pagamento:
    print(f"\nO valor do imóvel é: {valor_Casa:.2f}, seu salario e: {valor_Salario:.2f},")
    print(f"Cálculo de meses: {total_Anos} anos, são {meses} meses.")
    print(f"O valor da parcela é: {parcela:.2f}, sendo possível a prestação limite: {pagamento:.2f}.")
    print("O financiamento é POSSÍVEL!")
else:
    print(f"\nO valor do imóvel é: {valor_Casa:.2f}, seu salario e: {valor_Salario:.2f},")
    print(f"Cálculo de meses: {total_Anos} anos, são {meses} meses.")
    print(f"O valor da parcela é: {parcela:.2f}, sendo possível a prestação limite: {pagamento:.2f}.")
    print("O financiamento não é POSSÍVEL!")
