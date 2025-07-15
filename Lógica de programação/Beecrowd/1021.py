#1021
valor = float(input())
valor_em_centavos = int(round(valor * 100))

# Notas
print("NOTAS:")
for nota in [10000, 5000, 2000, 1000, 500, 200]:
    qtd = valor_em_centavos // nota
    print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")
    valor_em_centavos %= nota

# Moedas
print("MOEDAS:")
for moeda in [100, 50, 25, 10, 5, 1]:
    qtd = valor_em_centavos // moeda
    print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")
    valor_em_centavos %= moeda