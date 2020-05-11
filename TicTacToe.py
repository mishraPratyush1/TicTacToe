# ----global variables-----

# game board
board=["-","-","-",
	   "-","-","-",
	   "-","-","-",]

# if game is still game_still_going
game_still_going=True

# who won or tie
winner=None

# whose turn is it
current_player="X"

def display():
	print(board[0]+"|"+board[1]+"|"+board[2])
	print(board[3]+"|"+board[4]+"|"+board[5])
	print(board[6]+"|"+board[7]+"|"+board[8])

def play():
	
	display()

	while game_still_going:
		
		handle_turn(current_player)

		check_if_game_over()

		flip_player()

	# game has ended
	if winner == "X" or winner == "O":
		print(winner+" won.")
	elif winner==None:
		print("Tie.")

	

def handle_turn(player):
	print(player+"'s turn")
	position=input('choose a position form 1 to 9: ')
	
	valid=False
	while not valid:
		while position not in ["1","2","3","4""5","6","7","8","9"]:
			position=input('choose a position form 1 to 9: ')
							

		position=int(position)-1
		
		if board[position] == "-":
			valid=True
		else:
			print("cannot go there")

	board[position]=player
	
	display()

def check_if_game_over():
	
	check_if_win()
	check_if_tie()


def check_if_win():

	global winner

	row_winner=check_rows()

	column_winner=check_columns()

	diagonal_winner=check_diagonal()

	if row_winner:
		winner=row_winner
	
	elif column_winner:
		winner=column_winner
	
	elif diagonal_winner:
		winner=diagonal_winner
	
	else:
		winner=None

	# check diags,columns,diagonals
	return

def check_rows():

	global game_still_going
	
	diag_1 = board[0] == board[1] == board[2] != "-"
	diag_2 = board[3] == board[4] == board[5] != "-"
	diag_3 = board[6] == board[7] == board[8] != "-"

	if diag_1 or diag_2 or diag_3:
		game_still_going=False
	if diag_1:
		  return board[0]
	elif diag_2:
		return board[3]
	elif diag_3:
		return board[6]
	return
	

def  check_columns():
	global game_still_going
	
	col_1 = board[0] == board[3] == board[6] != "-"
	col_2 = board[1] == board[4] == board[7] != "-"
	col_3 = board[2] == board[5] == board[8] != "-"

	if col_1 or col_2 or col_3:
		game_still_going=False
	if col_1:
		  return board[0]
	elif col_2:
		return board[1]
	elif col_3:
		return board[2]
	return
def check_diagonal():
	global game_still_going
	
	diag_1 = board[0] == board[4] == board[8] != "-"
	diag_2 = board[2] == board[4] == board[6] != "-"
	

	if diag_1 or diag_2:
		game_still_going=False
	if diag_1:
		  return board[0]
	elif diag_2:
		return board[2]
	
	return


def check_if_tie():
	global game_still_going
	if "-" not in board:
		game_still_going=False
	
	return

def flip_player():

	global current_player

	if current_player == "X":
		current_player ="O"
	else:
		current_player = "X"
	return

play()

