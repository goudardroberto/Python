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

# Exemplo 3
# for i in range(1, 10):
#     print(i)
# print("Fim!")

# Criar uma variável contador para ter controle do looping
# i = 1
# while i < 10:
#     print(i)
      # Incrementar a variável para ter um fim
#     i += 1
# print("Fim!")

# Exemplo 4
# for i in range(1, 5):
#     n = input("Entre com um valor: ")
# print("Fim!")

# i = 1
# while i < 5:
#     n = input("Entre com um valor: ")
#     i += 1
# print("Fim!")

# Exemplo 5
# Também podemos inserir a condição para a saída do looping ao digitar 0
# i = 1
# while i != 0:
      # Aqui precisamos passar a variável para inteiro
#     i = int(input("Entre com um número: "))
# print("Fim!")

# Exemplo 6
# Podemos separar a condição para saída em outra variável
# i = "S"
# while i == "S":
#     n = int(input("Entre com um valor: "))
#     i = str(input("Quer continuar [ S/N ]: ")).upper()
# print("Fim!")

# Exemplo 7
# Quando amarrar o 0 para saída do looping, sempre criar condição para não contabilizar ele
n = 1
par = impar = 0
while n != 0:
    n = int(input("Entre com um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares!".format(par, impar))
