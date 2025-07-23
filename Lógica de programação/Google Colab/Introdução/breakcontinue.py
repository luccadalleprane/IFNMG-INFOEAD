for i in range(5):
	if i == 0:
		print('i = 0, Então: ', i)
	elif i == 1:
		print('i = 1, Então: continue')
		continue
	elif 1 < i < 3:
		print('A variável i, é: ', i)
	elif i == 3:
		print('i = 3, Então: break')
		break
	else:
		print('i > 3, Então: ', i)
print('Fim do loop')
