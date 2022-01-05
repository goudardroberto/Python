"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"Sua nota foi: {nota1} e {nota2}, sua média foi: {media} e você está REPROVADO!")
# media >= 5 and media < 7
elif 7 > media >= 5.0:
    print(f"Sua nota foi: {nota1} e {nota2}, sua média foi: {media} e você está em RECUPERAÇÃO!")
elif media >= 7.0:
    print(f"Sua nota foi: {nota1} e {nota2}, sua média foi: {media} e você está APROVADO!")
