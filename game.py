from main import TicTacToe
import time


def helptext(game1):
	print("!Welcome to the help section!")
	time.sleep(2)
	print("It is same as you played in the real life.")
	time.sleep(2)
	print("But the marking of X and O in the field is different in this game.")
	time.sleep(2)
	print("To mark the X and O in the layout this game uses numeric values. Each place represents a number range 1 and 9.")
	time.sleep(2)
	print("To understand more the layout with their respective numbers is shown below.")
	time.sleep(2)
	print()
	game1.locationhelper()
	print('\n'*1)
	print("I hope you understand how to use the marking system\n\n Let's test your understanding with a quick example!")
	print('\n'*1)
	game1.exampleset()
	print('\n'*1)

def play():
	game1=TicTacToe()
	print('Welcome to the game of Tic-Tac-Toe')
	time.sleep(1)
	print('If you are trying my version of this game, I suggest you to select the help option next and then continue the game')
	time.sleep(1)
	if input('Do you want to read help section(y/n)?:').lower()=='y':
		helptext(game1)
	time.sleep(1)
	print('-'*25)
	print("let's play the game!")
	print('-'*25)
	print('\n\n')
	time.sleep(1)
	p1=input("Enter the name of player choosing X: ")
	time.sleep(1)
	p2=input("Enter the name of player choosing O: ")
	map={'X':p1,'O':p2}
	time.sleep(1)
	sequence=['X','O','X','O','X','O','X','O','X','O']
	choice=input('Who is going to start first "X" or "O" (default is "X") ?')
	if choice.lower()=='o':
		sequence=sequence[1:]

	i=0
	while(i<9):
		turn=sequence[i]
		move=int(input(f"Enter the location you want to mark {turn} :"))
		if (move>=1 and move<=9):
			game1.valueupdater(move,turn)
			game1.showground()
			i=i+1
		else:
			print("Please enter a valid position in the range of (1-9)")
		if game1.checkstraight():
			print('-'*25)
			print(f"{map[turn]} wins!!!")
			print('-'*25)
			game1.showground()
			break
		if game1.checkdiagonal():
			print('-'*25)
			print(f"{map[turn]} wins!!!")
			print('-'*25)
			game1.showground()
			break
	if i==9:
		print('-'*25)
		print('!It is a tie!')
		print('-'*25)
		
	if input("I hope you enjoyed the game! Do you want to play one more time(y/n):").lower()=='y':
		play()

play()

