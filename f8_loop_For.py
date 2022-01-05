"""
Loop for

loop -> Estrutura de repetição
For -> Uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

"""

nome = "Roberto"
lista = [1, 2, 3, 4, 5]

"""

Exemplos de iteraveis:
Range -> Intervalo
    - O primeiro parâmetro é o início do intervalo
    - O segundo parâmetro é o final do intervalo excluindo o próprio número
        for i in range(1, 10):
        print(i)

String, ele percorre toda ela
    for i in nome:
        print(i)

Lista
    for i in lista:
        print(i)
"""

# O enumerate retorna índice e valor, podemos imprimir as letras, as posições das letras ou tudo
# for indice, letra in enumerate(nome):
#     print(indice, letra)

"""
Para encontrar a posição de um caractere em uma sting, podemos usar o:
find()
rfind()
index()

Exemplo:
print(nome.find("e"))
"""

# Controlando o looping com valor passado pelo usuário
# qtd = int(input("Quantas vezes o looping deve rodar? "))
# for n in range(1, qtd + 1):
#     print(n)

""" 
Site dos códigos emojis -> https://apps.timwhitlock.info/emoji/tables/unicode
- Trocar o + por 000
- Não esquecer a barra inversa \

Criando uma metade de triângulo
emoji = "\U0001F603"
for i in range(1, 10):
    print(i * nome)
    
Criando uma metade de triângulo inverso
for i in range(10, 1, -1):
    print(i * nome)
"""

emoji = "\U0001F603"
for i in range(1, 10):
    print(i * emoji)
for i in range(10, 0, -1):
    print(i * emoji)
