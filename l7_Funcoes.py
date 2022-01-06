"""
### Funções

# Definindo uma função
def primeiraFunc():
    print('Hello World')

primeiraFunc()


# Definindo uma função com parâmetro
def primeiraFunc(nome):
    print('Hello %s' %(nome))

primeiraFunc('Aluno')


def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))

funcLeitura()
# Out
# Número 0
# Número 1
# Número 2
# Número 3
# Número 4

# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a função e passando parâmetros
addNum(45, 3)
# Out
# Primeiro número: 45
# Segundo número: 3
# Soma:  48

# Variáveis locais e globais

# Variável Global
var_global = 10  # Esta é uma variável global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiply(5, 25)
# Out
# 125

print(var_global)
# Out
# 10

# Variável Local
var_global = 10  # Esta é uma variável global
def multiply(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

multiply(5, 25)
# Out
# 125

print(var_local)
# Out
# ERROR

# Funções Built-in
abs(-56)
# Out
# 56

abs(23)
# Out
# 23

bool(0)
# Out
# False

bool(1)
# Out
# True

# Funções str, int, float

# Erro ao executar por causa da conversão
idade = input("Digite sua idade: ")
if idade > 13:
    print("Você pode acessar o Facebook")  
# Out
# Digite sua idade: 18
# ERROR

# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar o Facebook")  
# Out
# Digite sua idade: 18
# Você pode acessar o Facebook

int("26")
# Out
# 26

float("123.345")
# Out
# 123.345

str(14)
# Out
# '14'

len([23,34,45,46])
# Out
# 4

array = ['a', 'b', 'c']
max(array)
# Out
# 'c'

min(array)
# Out
# 'a'

array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
array
# Out
# ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

max(array)
# Out
# 'd'

min(array)
'A'

list1 = [23, 23, 34, 45]
sum(list1)
# Out
# 125

# Criando funções usando outras funções
# In
import math

def numPrimo(num):
    '''
    Verificando se um número 
    é primo. 
    '''
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

numPrimo(541)
# Out
# 'Este número é primo'

# Fazendo split dos dados
def split_string(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."

# Isso divide a string em uma lista.
print(split_string(texto))
# Out
# ['Esta', 'função', 'será', 'bastante', 'útil', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados.']

# Podemos atribuir o output de uma função, para uma variável
token = split_string(texto)

token
# Out
['Esta',
 'função',
 'será',
 'bastante',
 'útil',
 'para',
 'separar',
 'grandes',
 'volumes',
 'de',
 'dados.']

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

lowercased_string
# Out
# 'este texto deveria estar todo em lowercase'

# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;

# Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)
# Out
# O parâmetro passado foi:  10

printVarInfo('Chocolate', 'Morango', 'Banana')
# Out
# O parâmetro passado foi:  Chocolate
# O parâmetro passado foi:  Morango
# O parâmetro passado foi:  Banana
"""
