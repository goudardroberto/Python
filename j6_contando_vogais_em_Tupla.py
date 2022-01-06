"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMAR', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos ", end="")
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=" ")
