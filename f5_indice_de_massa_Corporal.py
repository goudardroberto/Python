""""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input("Entre com seu peso: "))
altura = float(input("Entre com sua altura: "))

# altura ao quadrado = altura ** 2
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu imc é {imc:.2f} e você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu imc é {imc:.2f} e você está no peso ideal.")
elif 25 <= imc < 30:
    print(f"Seu imc é {imc:.2f} e você está com sobrepeso.")
elif 30 <= imc < 40:
    print(f"Seu imc é {imc:.2f} e você está com obesidade.")
elif imc >= 40:
    print(f"Seu imc é {imc:.2f} e você está com obesidade mórbida")
