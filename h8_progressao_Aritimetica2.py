"""Lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end="")
    # termo = termo + razao
    termo += razao
    cont += 1
print("Fim!")
