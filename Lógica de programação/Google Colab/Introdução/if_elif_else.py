# ---title: "if, elif e else"
# ---description: "Entenda como funcionam os condicionais em Python"
# Em Python, os operadores condicionais são o if e o else. A partir destes, existe
# a ramificação elif , que é a junção do if com o elif para indentar os condicionais
# em sequência lógica.

a = input('Digite um número: ')
b = input('Digite outro número: ')
if b > a:
    c = 'is cool!'
elif a == b:
    c = "isn't cool!"
else:
    c = "isn't cool!"
a = 'Apostila '
b = 'of Python '
print(a + b + c)
