"""
Tipo Booleano

Algebra Booleana, criada por George Boole

Duas constantes => Verdadeiro ou Falso

True => Verdadeiro
False => Falso

OBS: Sempre com a inicial maiúscula
"""

ativo = True
print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Se a negação for de um valor verdadeiro o resultado será falso
Se a negação for de um valor falso o resultado será verdadeiro
"""
print(not ativo)

logado = True

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True => True
True or False => True
False or True => True
False or False => False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores, ambos os valores devem ser verdadeiro.
True or True => True
True or False => False
False or True => False
False or False => False
"""
print(ativo and logado)

"""
Exemplos:
"""
# 5 > 6
# False

# 5 < 6
# True

# 6 == 6
# True

# 4 <= 5
# True

# num1 = 7
# num2 = 8
# num1 >= num2
# False

# num1 < num2 or num2 > 10
# True

# type(False)
# <class 'bool'>

# ativo = True
# type(ativo)
# <class 'bool'>
# dir(ativo) 
