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

Exemplos de operações:
- Soma
# 4 + 4
8

- Subtração
# 4 - 3
1

- Multiplicação
# 3 * 3
9

- Divisão
# 3 / 2
1.5

- Potência
# 4 ** 2
16

- Módulo
# 10 % 3
1

- Operações com float
# 3.1 + 6.4
9.5

# 4 + 4.0
8.0

# 4 + 4
8

# 4 / 2
2.0

# 4 // 2
2

# 4 / 3.0
1.3333333333333333

# 4 // 3.0
1.0

- Conversão

# float(9)
9.0

# int(6.0)
6

# int(6.5)
6

- Hexadecimal e Binário

# hex(394)
'0x18a'

# hex(217)
'0xd9'

# bin(286)
'0b100011110'

# bin(390)
'0b110000110'

- Funções abs, round e pow

- Retorna o valor absoluto
# abs(-8)
8

- Retorna o valor absoluto
# abs(8)
8

- Retorna o valor com arredondamento
# round(3.14151922,2)
3.14

- Potência
# pow(4,2)
16

- Potência
# pow(5,3)
125
"""
