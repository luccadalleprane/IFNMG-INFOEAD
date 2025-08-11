#1064
contador = 0
soma = 0
for i in range(6):
    num = float(input())
    if num > 0:
        soma += num
        contador += 1
average = soma / contador
print(f"{contador} valores positivos")
print(f"{average:.1f}")
