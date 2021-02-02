import itertools

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

def checkstraight():
	#print(list(itertools.combinations_with_replacement([0,1,2],2)))
	h_loc=[]	
	v_loc=[]
	for i in range(3):
		hi_loc=[]
		vi_loc=[]
		for j in range(3):
			hi_loc.append((i,j))
			vi_loc.append((j,i))
		h_loc.append(hi_loc)
		v_loc.append(vi_loc)
	for item in h_loc:
		if (ground[item[0][0]][item[0][1]]==ground[item[1][0]][item[1][1]]==ground[item[2][0]][item[2][1]] and ground[item[0][0]] != ' '):
			print('Got a match')
	for item in v_loc:
		if (ground[item[0][0]][item[0][1]]==ground[item[1][0]][item[1][1]]==ground[item[2][0]][item[2][1]] and ground[item[0][0]] != ' '):
			print('Got a match')		
def checkdiagonal():
	diag1=[(0,0),(1,1),(2,2)]
	diag2=[(0,2),(1,1),(2,0)]
	if (ground[diag1[0][0]][diag1[0][1]]==ground[diag1[1][0]][diag1[1][1]]==ground[diag1[2][0]][diag1[2][1]] and ground[diag1[0][0]] != ' '):
		print('Got a match')
	elif (ground[diag2[0][0]][diag2[0][1]]==ground[diag2[1][0]][diag2[1][1]]==ground[diag2[2][0]][diag2[2][1]] and ground[diag2[0][0]] != ' '):
		print('Got a match')
#ground=[[0]*3]*3
ground=[[0,2,6],[1,0,0],[1,6,0]]
checkstraight()
#showground()
checkdiagonal()
#print(ground[0][0])
