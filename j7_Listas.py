"""
Listas

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possui tamanho fixo. Podemos criar a lista e ir adicionando elementos.
  Enquanto houver memória disponível.
- Qualquer tipo de dado: Não possuem tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado.

As listas em python são representadas entre colchetes: []

# Descobrindo se é uma lista

type([])

# Exemplos:

# Podemos facilmente checar se determinado valor está contido na lista
numero = int(input("Qual número você quer encontrar na lista 4? "))

if numero in lista4:
    print(f"Encontrei o {numero}!")
else:
    print(f"Não encontrei o {numero}!")

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
# Na lista1 o número 1 apareceu 2 vezes
print(lista1.count(1))
# Na lista5 o 't' apareceu 1 vez
print(lista5.count('t'))

# Para adicionar elementos em listas, utilizamos a função append
  - O elemento por padrão entrará ao final da lista
  - Com append, só podemos adicionar 1 elemento por vez, ocorrendo erro caso possua mais parâmetros

print(lista1)
lista1.append(42)
print(lista1)

# Podemos adicionar uma lista com elementos dentro de uma lista
print(lista1)
lista1. append([8, 9, 'c'])
print(lista1)

x = int(input("O que deseja procurar? "))
if x in lista1:
    print(f"Encontrei na posição {lista1.index(x)}")

# Podemos colocar cada elemento da lista com valor adicional à lista com extend
  - Ele adiciona caso seja iterável, exemplo: listas, strings, tuplas, dicionários, conjuntos, etc..

lista1.extend('Roberto')
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
  - OBS - ISSO NÃO SUBSTITUI O VALOR NA POSIÇÃO, O MESMO SERÁ DESLOCADO PARA DIREITA

lista1.insert(2, '3')
print(lista1)

# Também podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Podemos printar na tela a ordem da lista conforme queremos, parecido com string
print(lista1)
# Ordem normal
print(lista1[::])
# Ordem inversa
print(lista1[::-1])

# Ou usando o reverse

lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Copiando uma lista
lista6 = lista2.copy()
print(lista6)

# Vendo quantos elementos possuem na lista (TAMANHO DA LISTA)
print(len(lista2))

# Podemos remover o último elemento de uma lista com pop
  - OBS: O pop não somente remove o último elemento mas também o retorna
  - Podemos passar o índice como parâmetro
  - Os elementos a direita são deslocados a esquerda
  - Se não houver elemento no índice informado, teremos o erro IndexError
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos converter facilmente uma string para uma lista
# Exemplo 1
# Por padrão, o split separa os elementos da lista pelo espaço entre elas
curso = "Python Programação Essencial"
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
# Podemos usar um parâmetro para divisão dos elementos ao converter a string para lista
curso = "Python,Programação,Essencial"
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string usando o join
# Aqui o join pega a lista, coloca espaço entre cada elemento e transforma em uma string
# Exemplo de separação -> '$', '/', ','...
print(lista7)
curso = " ".join(lista7)
print(curso)
print(type(curso))

# Iterando sobre listas

# Exemplo 1 utilizando for
# Lembrar que o tipo do elemento impacta no resultado
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input().strip()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto, end="; ")

# Utilizando variáveis em listas:
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Para encontrarmos a posição de um elemento usamos o index
cores = ['amarelo', 'verde', 'azul']
print(cores)
# Forma 1 -> retorna o índice
print(cores.index('verde'))
# Forma 2 -> retorna o elemento
print(cores[0])
print(cores[-1])
print(cores[-2])
print(cores[-3])

# Exemplos de for e while
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Percorrendo uma lista trazendo as cores e passando para letra maiúscula
for indice, cor in enumerate(cores):
    print(cor.upper())

# Gerando indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(34)
lista.append(27)
lista.append(42)
lista.append(30)
lista.append(58)
lista.append(27)
print(lista)

# Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista
# Caso o elemento não seja encontrado, retornará um erro
# Em qual índice da lista está o valor 6?

print(numeros.index(6))

# Em qual índice da lista está o valor 9?

print(numeros.index(9))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
# A leitura é feita passando a busca do primeiro parâmetro a partir do segundo parâmetro
# Se o segundo parâmetro for 1, a busca exclui o índice zero

print(numeros.index(5, 1))

# Podemos fazer busca dentro de um range início/fim
# Buscando o índice de valor 8, entre os índices de 3 ao 6
print(numeros.index(8, 3, 6))

# Revisão do slicing

# lista[início:fim:passo]
# range[início:fim:passo]

# Trabalhando com slice de lista com o parâmetro "início"
# Iniciando no índice 1 e pegando todos os elementos restantes
print(lista8[1:])

# Trabalhando com slice de lista com o parâmetro "fim"
# Começa em 0, pega até o índice 2 - 1
print(lista8[:2])
# Começa em 0, pega até o índice 4 - 1
print(lista8[:4])
# Começa do 1, pega até o índice 3 - 1
print(lista8[1:3])

# Trabalhando com o parâmetro "passo"
# Começa em 1, vai até o final, de 2 em 2
print(lista8[1::2])

# Começando em 0, vai até o final, de 2 em 2
print(lista8[::2])

# Invertendo valores em uma lista
nomes = ['Goudard', 'Roberto']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# Ou podemos usar o reverse
nomes = ['Goudard', 'Roberto']
nomes.reverse()
print(nomes)

# Soma; Valor Máximo; Valor Mínimo; Tamanho.
# Se os valores forem todos inteiros e reais
# Soma
print(sum(lista8))

# Valor Máximo
print(max(lista8))

# Valor Mínimo
print(min(lista8))

# Tamanho
print(len(lista8))

# Transformando uma lista em tupla
print(lista8)
print(type(lista8))

tupla = tuple(lista8)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
# Se tiver mais elementos para desempacotar do que variáveis para receber os valores, ocorrerá erro
num1, num2, num3 = lista8

print(num1)
print(num2)
print(num3)

# Copiando uma lista para (Shadow Copy e Deep Copy)
# Forma 1
# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista
# Mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra
# Isso em Python é chamado de Deep Copy (Cópia profunda)
lista9 = [1, 2, 3]
print(lista9)
nova = lista9.copy()
print(nova)
nova.append(4)
print(nova)

# Forma 2 - Shadow Copy
# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista
# Mas após realizar modificação em uma das listas, essa modificação se refletiu sem ambas as listas
# Isso em Python é chamado de Shadow Copy
lista9 = [1, 2, 3]
print(lista9)
nova = lista9
print(nova)
nova.append(4)
print(lista9)
print(nova)

"""

# Exemplos

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['R', 'o', 'b', 'e', 'r', 't', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Roberto Goudard')

lista6 = lista2.copy()

lista7 = ["Python", "Programação", "Essencial"]

cores = ['verde', 'amarelo', 'azul', 'branco']

numeros = [5, 6, 7, 8, 9, 10]

lista8 = [1, 2, 3]

"""
Listas de listas

# Criando uma lista com outra dentro
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

# SEM FAZER CÓPIA - Ao adicionar elementos dentro de listas já criadas, todos os elementos ficam iguais
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

# COM A CÓPIA - Ao adicionar elementos dentro de listas já criadas, não temos elementos replicados
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# Podemos retornar um elemento de uma lista dentro de outra lista
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
"""

# Pegando dados para adicionar a lista
galera = list()
dado = list()
totmai = totmen = 0


for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
