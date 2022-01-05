"""Perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        # termo = termo + razao
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")
