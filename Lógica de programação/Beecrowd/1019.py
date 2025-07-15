# 1019
A = int(input())
hours = A // 3600
A = A % 3600
minutes = A // 60
seconds = A % 60
print(f'{hours}:{minutes}:{seconds}')
