"""
Apresentando mensagem ao usuário

nome = input("Digite seu nome: ")
print("Olá", nome, "bem-vindo(a)!")

nome = input("Digite seu nome: ")
print(f"Olá {nome}, bem-vindo!")

Recebendo dados do usuário

input significa entrada

Qualquer dado recebido pelo input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Cast é a conversão de um tipo de dado para outro
- int(idade) => cast
"""
from datetime import date

# Entrando com dados
print("Qual o seu nome? ")
nome = input()
print(f"Seja bem-vindo(a) {nome}.", end="")

# Tirando os espaços com .strip()
# Passando para letra maiúscula com .upper()
# Fatiando a primeira letra da palavra com [0]
print(" Qual o seu sexo? ")
sexo = input().strip().upper()[0]

# Trazendo o dia atual e pegando o ano do resultado
# Passando a entrada do usuário para inteiro e passando o cálculo para idade
print("Quando você nasceu? ")
data = date.today().year
nascimento = int(input())
idade = data - nascimento

# Processando

# Saída de dados
# Criando uma condicional para separar o sexo e tratar possível erro
if sexo in "M":
    print(f"O {nome} tem {idade} anos.")
elif sexo in "F":
    print(f"A {nome} tem {idade} anos.")
else:
    print("Sexo incorreto!")
