from main import TicTacToe
game1=TicTacToe()
sequence=['X','O','X','O','X','O','X','O','X','O']
choice=input('Who is going to start first "X" or "O"?')
if choice.lower()=='o':
	sequence=sequence[1:]

for turn in sequence:
	move=int(input(f"Enter the location you want to mark {turn} :"))
	game1.valueupdater(move,turn)
	if game1.checkstraight():
		print(f"{turn} wins!!!")
		break
	if game1.checkdiagonal():
		print(f"{turn} wins!!!")
		break
	game1.showground()

