"""
Escopo de variáveis:

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, se escopo compreende todo o programa
Ex:
num = 5
print(num)

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarado

Exemplo, nesse caso como não entrou no bloco if, a variável não foi declarada, ocorrendo erro:
num = 5
if num > 10:
    local = num + 5
    print(local)
print(local)

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica.
Isso significa que ao declararmos uma variável,
nós colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuirmos o valor à mesma.

# Em Python podemos fazer a reatribuição, declarar a variável e mudar o tipo dela quantas vezes quisermos
numero = 42
print(numero)
print(type(numero))

numero = "Roberto"
print(numero)
print(type(numero))
"""

numero = 42
print(numero)
print(type(numero))

numero = "Roberto"
print(numero)
print(type(numero))
