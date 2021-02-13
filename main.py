import itertools

class TicTacToe():
	def __init__(self):
		self.ground=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

	def showgroun(self):
		for i in range(3):
			for j in range(3):
				if j==2:
					print(self.ground[i][j])
				else:
					print(self.ground[i][j],end=' | ')
			if i==2:
				print()
			else:
				print('-'*9)

	def valueupdater(self,x,value):
		loc_map={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
		self.ground[loc_map[x][0]][loc_map[x][1]]=value

	def checkstraight(self):
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
			if ((self.ground[item[0][0]][item[0][1]]==self.ground[item[1][0]][item[1][1]]==self.ground[item[2][0]][item[2][1]]) and self.ground[item[0][0]][item[0][1]]!=' '):
				return 1 

		for item in v_loc:
			if ((self.ground[item[0][0]][item[0][1]]==self.ground[item[1][0]][item[1][1]]==self.ground[item[2][0]][item[2][1]]) and self.ground[item[0][0]][item[0][1]]!=' '):
				return 1
					
	def checkdiagonal(self):
		diag1=[(0,0),(1,1),(2,2)]
		diag2=[(0,2),(1,1),(2,0)]
		if ((self.ground[diag1[0][0]][diag1[0][1]]==self.ground[diag1[1][0]][diag1[1][1]]==self.ground[diag1[2][0]][diag1[2][1]]) and self.ground[diag1[0][0]][diag1[0][1]]!=' '):
			return 1

		elif ((self.ground[diag2[0][0]][diag2[0][1]]==self.ground[diag2[1][0]][diag2[1][1]]==self.ground[diag2[2][0]][diag2[2][1]]) and self.ground[diag2[0][0]][diag2[0][1]]!=' '):
			return 1

