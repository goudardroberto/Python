"""
Tipo Float

Também conhecido como tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto

- Errado ao ponto de vista float mas gera uma tupla.
valor = 1, 44
print(valor)
print(type(valor))

- Certo do ponto de vista float.
valor = 1.44
print(valor)
print(type(valor))

- É possível fazer a dupla atribuição
valor1, valor2 = 1.5
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

- Podemos converter o float para int
- OBS: Perdemos precisão na conversão
valor = 1.44
res = int(valor)
print(res)
print(type(res))

OBS: Número e letra é um tipo complexo
valor = 1j
print(type(valor))
"""
