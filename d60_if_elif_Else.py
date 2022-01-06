"""
Estruturas condicionais
if, elif, else

- Exemplo 1:
nome = input("Digite seu nome: ")
if nome == "Roberto":
    print("Bem-vindo bonitão!")
else:
    print("Prazer!")
print("Tenha um bom dia {}!".format(nome))

- Exemplo 2:
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi: {:.1f}".format(m))
if m >= 6.0:
    print("Você esta aprovado!")
else:
    print("Você foi reprovado!")
print("---Fim___")

# if simplificado
print("Aprovado!" if m >= 6.0 else "Reprovado!")
"""

idade = 3

"""
- Se -> if (Podemos criar blocos condicionais if dentro de outros if para checar diversos parâmetros)
if idade > 4:
    print(f"A idade é {idade}.")

- Se não - elif (pode ser usado várias vezes para gerar inúmeras condições)
if idade >= 5:
    print(f"A idade é {idade}.")
elif idade == 4:
    print(f"A idade é {idade}.")

- Caso não - else (Aqui geralmente usamos condições genéricas para evitar erros)
if idade >= 5:
    print(f"A idade é {idade}.")
elif idade == 4:
    print(f"A idade é {idade}.")
else:
    print("A idade é menor que 4.")

"""
if idade >= 5:
    print(f"A idade é {idade}.")
elif idade == 4:
    print(f"A idade é {idade}.")
else:
    print("A idade é menor que 4.")
