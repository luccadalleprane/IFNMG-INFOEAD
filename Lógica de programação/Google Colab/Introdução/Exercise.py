# EXERCÍCIO
# Faça um programa que, dados dois números inteiros e um número real, calcule e mostre:
# (a = 15, b = -8, c = 4.6)
# - O produto do dobro do primeiro com a metade do segundo.
# - A soma do triplo do primeiro com o terceiro.
# - O terceiro elevado ao cubo.

a = 15
b = -8
c = 4.6

# Produto do dobro do primeiro com a metade do segundo
resultado = (a*2) * (b/2)
print(f'O produto do dobro do primeiro com a metade do segundo: {resultado}')

resultado = (a*3) + c  # Soma do triplo do primeiro com o terceiro
print(f'A soma do triplo do primeiro com o terceiro: {resultado}')

resultado = c ** 3  # Terceiro elevado ao cubo
print('O terceiro elevado ao cubo: {:.1f}'.format(resultado))
