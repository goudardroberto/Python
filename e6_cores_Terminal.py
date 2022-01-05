""" Aplicando cores no terminal
- Verificar o módulo colorize que possui mais funcionalidades
"""

a = 3
b = 5
# print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a, b))

# Fazendo de outra forma
# nome = "Roberto"
# print("Olá {}{}{}!!!".format("\033[4;34m", nome, "\033[m"))

# Utilizando dicionário
nome = "Roberto"
cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[7;30m"}
print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(cores["azul"], nome, cores["limpa"]))
