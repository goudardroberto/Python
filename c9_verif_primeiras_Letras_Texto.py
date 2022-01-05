""" Programa para ler o nome de uma cidade e diga se ela começa com o nome "Santo"""

cid = str(input("Digite o nome de uma cidade: ")).strip()
# Retorna um booleano
print(cid[:5].upper() == "SANTO")
