def showground():
	for i in range(3):
		for j in range(3):
			if j==2:
				print(ground[i][j])
			else:
				print(ground[i][j],end=' | ')
		if i==2:
			print()
		else:
			print('-'*9)
ground=[[0]*3]*3
showground()
#print(ground[0][0])
