""" Programa que lê um ângulo qualquer e retorna o seno, cosseno e tangente desse ângulo."""

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f"O ângulo informado foi: {angulo}")
print(f"Seu seno é: {sen:.2f}.")
print(f"Seu cosseno é: {cos:.2f}.")
print(f"Sua tangente é: {tan:.2f}.")
