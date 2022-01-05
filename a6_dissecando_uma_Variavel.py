"""Programa que lê algo pelo teclado e mostra na tela o seu tipo primitivo e
todas as informações possíveis sobre ele."""

# Toda str é um objeto que tem características e realiza funcionalidades
a = input("Digite algo: ")
# Toda entrada no input será considerada str pois o tipo primitivo não foi tratado
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaço? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúscula? ", a.isupper())
print("Está em minúscula? ", a.islower())
# Primeira maiúscula com o resto minúscula é tratada como palavra capitalizada
print("Está capitalizada? ", a.istitle())
