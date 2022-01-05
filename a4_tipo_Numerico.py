"""
Tipo numérico

Em primeiro momento, podemos considerar o int para inteiros => -1; 0; 1,
e o float para os números que apresentam casas decimais => 1.44; 3.2; 7.999

Para consultar o tipo da variável, usamos o type() e passamos a variável como parâmetro
# type(5.0)
float

# a = 'Eu sou uma string'
# type(a)
str

Tipo int

Soma = 1 + 1
Subtração = 1 - 1
Multiplicação = 1 * 1
Divisão = 1 / 1
Resto = 1 % 1
Quadrado = 2 ** 2
Cubo = 2 ** 3


# Exemplos de operações
# num = 2
# num = num + 2
num = 4

# Também podemos escrever assim:
# num = 2
# num += 2
num = 4

# num = 2
# num -= 2
num = 0

# num = 2
# num *= 2
num = 4

# num = 2
# num /= 2
num = 1.0
obs: Aqui por padrão o retorno será um float

# num 2
# num //= 2
num = 1

Tipo Float

Também conhecido como tipo real, decimal

OBS: O separador de casas decimais na programação é o ponto

- Errado ao ponto de vista float mas gera uma tupla.
# valor = 1, 44
# print(valor)
# print(type(valor))

- Certo do ponto de vista float.
# valor = 1.44
# print(valor)
# print(type(valor))

- É possível fazer a dupla atribuição
# valor1, valor2 = 1.5
# print(valor1)
# print(type(valor1))
# print(valor2)
# print(type(valor2))

- Podemos converter o float para int
- OBS: Perdemos precisão na conversão
# valor = 1.44
# res = int(valor)
# print(res)
# print(type(res))

OBS: Número e letra é um tipo complexo
# valor = 1j
# print(type(valor))
"""
