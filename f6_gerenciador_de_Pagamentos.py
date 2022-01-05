"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

print(f"{'Lojas Mais Barato':=^40}")
preco = float(input("Preço das compras: R$ "))
print("""Formas de pagamento
[ 1 ] à vista dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual a opção de pagamento? "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f"Total do valor para pagamento em dinheiro é {total} reais")
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f"Total do valor para pagamento no cartão de débito é {total} reais")
elif opcao == 3:
    parcela = preco / 2
    print(f"Total do valor para pagamento parcelado em 2x no cartão de crédito é {preco} reais "
          f"e cada parcela ficará em {parcela}")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print(f"O preço das compras é {preco} reais."
          f"\nO total do valor com juros é {total} reais."
          f"\nEm {totalparc} vezes no cartao as parcelas "
          f"saem a {parcela} reais por parcela")
