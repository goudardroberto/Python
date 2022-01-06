"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses (), mas criamos com a vírgula
    - tupla = (3,) -> Isso é uma tupla

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda. Toda operação
    em uma tupla gera uma nova tupla

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
# Aqui o python enxerga o 4 dentro do parênteses como int

tupla3 = (4)
print(tupla3)

print(type(tupla3))

# Aqui temos uma tupla
# Podemos concluir que na definição ela é tupla por causa da vírgula e não pelos parênteses
tupla4 = (4,)
print(tupla4)

print(type(tupla4))

# Podemos gerar uma tupla dinamicamente com range(início, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tuple))

# Desempacotamento de tupla
# Gera um erro se colocarmos um número diferente de elementos para desempacotar
tupla = ('Roberto Goudard', 'Rio de Janeiro: Brasil')
nome, residencia = tupla
print(nome, residencia)

# Métodos para adoção e remoção de elementos nas tuplas não existem

# Soma; Valor Máximo; Valor Mínimo; Tamanho

# Se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
# Tuplas são imutáveis mas podemos concatenar seus valores em outra variável
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# Verificando um valor dentro de uma tupla, retorna verdadeiro ou falso
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
# Retorna quantas ocorrências de um mesmo elemento
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

# A tupla assim como a lista, ao passar uma string, podemos percorrê-la
nome = tuple('Roberto Goudard')
print(nome)

print(nome.count('o'))

# Dicas na utilização de tuplas
  - Devemos utilizar uma tupla SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
# Se fosse uma lista, outros elementos poderiam ser adicionados ou retirados
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril',
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro'
         )

print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual índice um elemento está na tupla
print(meses.index('Maio'))

# Slicing
# Tupla[início:fim:Passo]
print(meses[0:])
print(meses[:5])
print(meses[::2])

# Porquê utilizar tuplas?
  - São mais rápidas do que listas
  - Trabalhar com elementos imutáveis deixa o código mais seguro

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)
"""

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril',
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro'
         )
