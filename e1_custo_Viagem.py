"""Programa que solicita a distância de uma viagem em km
cobrando R$ 0,50 por km para viagens até 200 km
R$ 0,45 para viagens mais longas"""

km = float(input("Entre com a kilometragem da viagem: "))
print(f"Para uma viagem de {km} km")
# if km <= 200:
#     valor = km * 0.50
# else:
#     valor = km * 0.45

# if simplificado
valor = km * 0.50 if km <=200 else km * 0.45
print(f"O custo da viagem fica em: {valor:.2f} reais")
