# 1101
while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if m < n:
        menor = m
        maior = n
    else:
        menor = n
        maior = m
    soma = 0
    for i in range(menor, maior + 1):
        print(i, end=" ")
        soma += i
    print(f"Sum={soma}")
