# 1013
a = int(input())
b = int(input())
c = int(input())

maiorAB = (a + b + abs(a - b)) // 2
maior = (maiorAB + c + abs(maiorAB - c)) // 2

print(f'{maior} eh o maior')
