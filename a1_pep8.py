"""
PEP8 - Python Enhancement Proposal

O que é? São respostas de melhorias para a Linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

Exemplos (Todos são PEP8):

[1] Utilize Camel Case para nomes de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] Utilize nomes em letras minúsculas, separados por underline para funções ou variáveis;


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] Utilize 4 espaços para identação! obs: Alguns computadores possuem configurações diferentes do Python;

if 'a' in 'banana':
    print('Tem')

[4] Linhas em branco.
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] Imports
- Imports devem ser colocados no topo do arquivo. Logo depois de quaisquer comentários ou
docstrings e antes de constantes ou variáveis globais.
- Imports devem ser sempre feitos em linhas separadas;
- Importando o pacote completo, fazemos assim:

import sys
import os

- Se for uma classe do pacote, no máximo 3 objetos, podemos fazer assim:

from types import StringType, ListType

- No caso de vários imports, podemos fazer assim:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

[6] Espaços em expressões e instruções
- Não faça:

funcao( algo[ 1 ], { outro: 2 } )

- Faça:

funcao(algo[1], {outro: 2})

[7] Termine sempre uma instrução com uma nova linha
"""
