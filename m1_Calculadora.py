# Definindo as funções
def adi(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Criando as condicionais das equações
print("****************Calculadora****************\n")
print("Escolha a operação que deseja realizar:\n1-Adição; \n2-Subtração; \n3-Multiplicação; \n4-Divisão. \n")

escolha = input("Digite a operação: ")

num1 = int(input("\nDigite o primeiro valor: "))
num2 = int(input("\nDigite o segundo valor: "))

if escolha == "1":
    print("\n")
    print(num1, "+", num2, "=", adi(num1, num2))
    print("\n")

elif escolha == "2":
    print("\n")
    print(num1, "-", num2, "=", sub(num1, num2))
    print("\n")

elif escolha == "3":
    print("\n")
    print(num1, "*", num2, "=", mul(num1, num2))
    print("\n")

elif escolha == "4":
    print("\n")
    print(num1, "/", num2, "=", div(num1, num2))
    print("\n")

else:
    print("\nOpção Inválida!")
