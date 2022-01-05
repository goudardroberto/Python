""" Programa que lê a largura e a altura de uma parede em metros,
calcula a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

# Cálculo: largura x altura = m2

print("Calcule a medida de tinta necessária para pintar uma parede: ")
largura = float(input("Entre com a largura da parede: "))
altura = float(input("Entre com a altura da parede: "))
resultado = largura * altura

print(f"Sua parede tem dimensões de {largura} x {altura} e sua área é de {resultado} m2")

# 1l = 7.7 m2

litro = resultado / 7.7
print("Você precisará de {litro:.2} l de tinta.")
