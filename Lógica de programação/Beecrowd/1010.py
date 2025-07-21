#1010
# Lê as linhas
line1 = input()
line2 = input()
# Separa os dados e converte
cod1, num1, unit1 = line1.split()
cod1 = int(cod1)
num1 = int(num1)
unit1 = float(unit1)
cod2, num2, unit2 = line2.split()
cod2 = int(cod2)
num2 = int(num2)
unit2 = float(unit2)
# Calcula total
total = (num1 * unit1) + (num2 * unit2)
# Exibe o resultado
print(f'VALOR A PAGAR: R$ {total:.2f}')
