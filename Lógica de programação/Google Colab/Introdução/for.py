#Encontrar a soma S = 1+4+7+10+13+16+19
# S = 1 + 3n, onde n é o número de termos
# Imprime a soma S
s = 0
for i in range(1, 20, 3):
    s += i
print('Soma = ',s)