""" Programa que lê um número e mostra seu dobro, triplo e raíz."""

# Usando função pow(), usando a potência elevado a meio obtemos o resultado da raíz
res = int(input("Entre com um número: "))
print(f"O dobro é: {(res * 2)};\n")
print(f"Seu triplo é: {(res * 3)} e sua raíz é: {pow(res, (1/2))}.")

# Sem importar pacote
# res = int(input("Entre com um número: "))
# dob = res * 2
# trip = res * 3
# raiz = res ** (1/2)
# print("O número apresentado foi {res}, seu dobro é: {dob}, seu triplo é: {trip} e sua raíz é: {raiz}.")

# Importando pacote
# import math

# res = int(input("Entre com um número: "))
# dob = res * 2
# trip = res * 3
# raiz = math.sqrt(res)
# {2f} quer dizer duas casas decimais flutuantes
# print("O número apresentado foi {res}, seu dobro é: {dob}, seu triplo é: {trip} e sua raíz é: {raiz:2f}.")
