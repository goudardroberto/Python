"""A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date

ano_Atual = date.today().year
nasc = int(input("Entre com ano de nascimento do atleta: "))
idade = ano_Atual - nasc

if 0 < idade <= 9:
    print(f"O atleta tem {idade} anos e está dentro da categoria MIRIM")
elif 9 < idade <= 14:
    print(f"O atleta tem {idade} anos e está dentro da categoria INFANTIL")
elif 14 < idade <= 19:
    print(f"O atleta tem {idade} anos e está dentro da categoria JÚNIOR")
elif 19 < idade <= 25:
    print(f"O atleta tem {idade} anos e está dentro da categoria MASTER")
elif 25 < idade < 100:
    print(f"O atleta tem {idade} anos e está dentro da categoria SÊNIOR")
elif 100 <= idade <= 110:
    print(f"O atleta tem {idade} anos. Consulte a possibilidade da participação do atleta.")
else:
    print("Idade incompatível!")
