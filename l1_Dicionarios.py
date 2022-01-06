"""
Dicionários

# Exemplo 1
filmes = {'Star Wars': 'título', '1997': 'ano', 'George Lucas': 'diretor'}

print(filmes.values())
print(filmes.keys())
print(filmes.items())

# Usando for
for k, v in filmes.items():
    print(f"O {k} é o {v}")

# Dicionários dentro de listas
locadora = list()
locadora.append(filmes)
print(locadora)

# Exemplo 2
pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

# Apagando elementos com del
del pessoas['Sexo']
print(pessoas)

# Adicionando elementos - Não é necessário o append
pessoas['peso'] = 98
print(pessoas)

# Exemplo 3
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
