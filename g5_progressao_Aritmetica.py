"""Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro_Termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro_Termo + (10 - 1) * razao

for i in range(primeiro_Termo, decimo + razao, razao):
        print(i)
print("Fim!")
