"""
Tipo String

- Toda entrada do input será do tipo string
- Em Python, toda string estará entre:
- Aspas simples -> 'uma string', '234', 'a', 'True', '42.2'
- Aspas duplas -> "uma string", "234", "a", "True", "42.2"
- Aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.2'''

# Para pular uma linha usamos o \n dentro da string
nome = "Roberto \nRamos"
print(nome)

# Para colocar uma aspas dupla no meio de duas, podemos usar um caractere especial
nome = "Roberto \" Ramos"
print(nome)
print(type(nome))

# Passando tudo para letra maiúscula com .upper()
nome = "Roberto Ramos"
print(nome.upper())

# Passando tudo para letra minúscula com .lower()
nome = "Roberto Ramos"
print(nome.lower())

# Passando a string para lista, separando pelo espaço
nome = "Roberto Ramos"
print(nome.split())

# Podemos passar a posição para retornar um elemento da lista
nome = "Roberto Ramos"
print(nome.split()[0])

# Podemos fatiar a string, o segundo parâmetro é excludente (Slice de String)
nome = "Roberto Ramos"
print(nome[0:7])

nome = "Roberto Ramos"
print(nome[8:13])

# podemos trazer a string ao contrário
# O primeiro : é o início; O segundo : é o final
nome = "Roberto Ramos"
print(nome[::-1])

# Tirando os espaços do início e do final da string
nome = "    Roberto Ramos    "
print(nome.strip())

# Para saber o tamanho da string usamos o len() passando a variável como parâmetro
nome = "Roberto Ramos"
print(len(nome))

# Também conseguimos mudar as letras dentro de uma string com replace
nome = "Roberto Ramos"
print(nome.replace("o", "a"))
"""
# - Aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.2"""

nome = "Roberto Ramos"
print(nome.replace("o", "a"))
