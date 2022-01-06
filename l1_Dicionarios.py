"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

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

print(type({}))

"""
OBS: Sobre dicionários
- Chave e valor são separados por dois pontos 'chave': 'valor'

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
# OBS: Ao tentarmos fazer um acesso utilizando uma chave que não existe, teremos um erro
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('py'))

# O None sempre será falso
# Podemos passar um default
# O segundo parâmetro é reconhecido como valor -> ex: russia = paises.get('ru', 'Não encontrado')
# Nesse caso o retorno passa a ser positivo caso entre numa condicional
# No exemplo abaixo o retorno é falso
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
russia = paises.get('ru')
if russia:
    print('Encontrei o país')
else:
    print('Não encontrei o país')

print(type(russia))

# Ao buscar, um elemento no dicionário, ele só retornará se a busca for por alguma chave
# Ele não retornará valor
# O retorno será um booleano
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos usar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário
# como chave de dicionários

# Tuplas por exemplo são bastante interessantes de serem usadas como chaves de dicionários,
# pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório de Tóquio',
    (40.7128, 74.0060): 'Escritório de Nova York',
    (37.7749, 122.4194): 'Escritório de São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados um um dicionário é a mesma
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas, ele atualiza o último elemento caso já exista

# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1
# OBS 1: Aqui a gente passa a chave para remover o elemento, se não encontrar a chave ocorrerá erro
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado
ret = receita.pop('mar')
print(ret)

# Forma 2
# Se a chave não existir será gerado um erro
del receita['fev']
print(receita)
"""

# Porquê usamos dicionários?
# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras onde adicionamos produtos

"""
Carrinho
de
compras:
Produto
1:
- Nome;
- Quantidade;
- Preço;
Produto
2:
- Nome;
- Quantidade;
- Preço;

# Poderíamos fazer com listas, porém precisaríamos saber o índice de cada informação no produto
# Poderíamos fazer com tuplas, porém precisaríamos saber o índice de cada informação no produto

# Ao utilizar o dicionário facilmente adicionamos ou removemos produtos e em cada produto podemos
# ter a certeza sobre cada informação
carrinho = []

produto1 = {'Nome': 'Play Station 4', 'Quantidade': 1, 'Preço': 3000.00}
produto2 = {'Nome': 'God of War 4', 'Quantidade': 1, 'Preço': 250.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print(type(carrinho))

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro
Forma
1
novo = d.copy()  # Deep copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow copy
novo = d

print(novo)
novo['d'] = 4

print(d)

# Forma não usual de criação de dicionários
# O método fromkeys recebe dois parâmetros: Um iterável e um valor
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)"""