#1159
while True:
    x = int(input())
    if x == 0:
        break
    soma = 0  # inicializa soma antes do loop
    if x % 2 == 0:
        inicio = x  # se for par, começa em x
    else:
        inicio = x + 1  # se for ímpar, começa no próximo par
    for i in range(5):
        soma += inicio + 2 * i  # soma os pares consecutivos
    print(soma)
