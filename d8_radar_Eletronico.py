"""Programa que lê a velocidade do carro, 
se a velocidade for superior a 80km diz que foi multado, 
a multa vai custar 7 reais por km acima do limite"""

velocidade = float(input("Qual é a velocidade atual do carro? "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"O limite da pista é de 80km/h .Você foi multado! Sua multa é de: {multa} reais!")
else:
    print("Tenha um bom dia! Dirija com segurança!")
