# Lê o valor inteiro
valor = int(input())
# Imprime o valor (linha inicial obrigatória)
print(valor)
# Lista de notas
notas = [100, 50, 20, 10, 5, 2, 1]
# Para cada nota, calcula e imprime a quantidade
for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R$ {nota},00")
    valor %= nota
