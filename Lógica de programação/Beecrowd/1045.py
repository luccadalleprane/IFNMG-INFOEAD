# 1045
# Entrada de dados
valores = list(map(float, input().split()))
# Ordena os valores em ordem decrescente
valores.sort(reverse=True)
a, b, c = valores
# Verifica se é possível formar um triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
# Classificação por ângulos
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
# Classificação por lados
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
  print("TRIANGULO ISOSCELES")
