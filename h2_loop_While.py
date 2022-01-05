"""
Loop While

# Forma geral:

while expressao_booleana
    //execucao do loop

- O bloco do while será repetido enquanto a expressão booleana for verdadeira

- Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplo:

num = 5

num < 5

# Exemplo 1
- Em um loop while é importante que cuidemos do critério de parada para não causar loop infinito

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Exemplo 2

resposta = ""
while resposta != "S":
    resposta = input("Já acabou Jéssica? ").strip().upper()[0]
"""
