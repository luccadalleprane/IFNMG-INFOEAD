# 1038
# Entrada de dados
x, y = map(int, input().split())
# Calcula o valor do produto
if x == 1:
    total = y * 4.00
elif x == 2:
    total = y * 4.50
elif x == 3:
    total = y * 5.00
elif x == 4:
    total = y * 2.00
elif x == 5:
    total = y * 1.50
else:
    total = 0
# Calcula o total
print(f'Total: R$ {total:.2f}')