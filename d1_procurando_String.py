""" Programa que lê um nome e verifica se tem "Silva" no nome."""

# Para evitar a busca selecionada, importante passar a palavra pra maiúscula antes Utilizando o operador in

nome = str(input("Digite seu nome: ")).strip()
print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")
