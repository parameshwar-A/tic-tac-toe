from main import TicTacToe
game1=TicTacToe()
p1=input("Enter the name of player choosing X: ")
p2=input("Enter the name of player choosing O: ")
map={'X':p1,'O':p2}
sequence=['X','O','X','O','X','O','X','O','X','O']
choice=input('Who is going to start first "X" or "O" (default is "X") ?')
if choice.lower()=='o':
	sequence=sequence[1:]

for turn in sequence:
	move=int(input(f"Enter the location you want to mark {turn} :"))
	if (move>=1 and move<=9):
		game1.valueupdater(move,turn)
	else:
		print("Please enter a valid position in the range of (1-9)")
	if game1.checkstraight():
		print(f"{map[turn]} wins!!!")
		game1.showground()
		break
	if game1.checkdiagonal():
		print(f"{map[turn]} wins!!!")
		game1.showground()
		break
	game1.showground()

