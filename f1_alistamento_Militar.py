"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

# ano_Nascimento = int(input("Entre com o ano do seu nascimento: "))
# ano_Atual = 2021
# resultado = ano_Atual - ano_Nascimento
# falta = (resultado - 18) * (-1)

# if resultado >= 0 and resultado < 17:
#     print(f"Você ainda tem {falta} anos para o alistamento militar obrigatório!")
# elif resultado >= 17 and resultado <= 18:
#     print("Você precisa dar entrada para se apresentar às forças armadas")
# elif resultado > 19:
#     print(f"Você passou {falta} anos da apresentação e está em falta com suas responsabilidades!")
# else:
#     print("Entre com uma idade positiva!")

from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
sexo1 = str(input("Entre com M para Masculino ou F para Feminino: "))
sexo2 = sexo1.upper()
idade = atual - nasc

if sexo2 == "M":
    print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")
    elif idade < 18:
        saldo = 18 - idade
        idade_Alistamento = saldo + atual
        print(f"Ainda faltam {saldo} anos para o alistamento")
        print(f"Seu alistamento será em {idade_Alistamento}")

    elif idade > 18:
        saldo = idade - 18
        idade_Alistamento = atual - saldo
        print(f"Você já deveria ter se alistado a {saldo} anos.")
        print(f"Seu alistamento foi em {idade_Alistamento}")
elif sexo2 == "F":
    print("O alistamento militar não é obrigatório para mulheres.")
    
