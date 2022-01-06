"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthias', 'Fortaleza',
         'Internacional', 'Fluminense', 'América-MG', 'Ceará', 'Athletico-PR', 'Santos',
         'Cuiabá', 'Atlético-GO', 'São Paulo', 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

# Todos os times
print("=-"*20)
print(f"A lista de times do brasileirão: {times}")

# Os 5 primeiros times.
print("=-"*20)
print(times[:5])

# Os últimos 4 colocados.
print("=-"*20)
print(times[-4:])

# Times em ordem alfabética.
print("=-"*20)
print(sorted(times))

# Em que posição está o time da Chapecoense.
print("=-"*20)
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}° posição.")
