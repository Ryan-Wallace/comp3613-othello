# Logan VanOostrum, Ryan Wallace, Ben McNutt

from random import choice

empty = '⋅'
black = 'B'
white = 'W'
border = '□'
adjacents = [-11, -10, -9, -1, +1, +9, +10, +11]
ai = ''

# print game board
def show_board(board):
	for i in range(10):
		for j in range(10):
			print(board.gameBoard[(i * 10) + j] + ' ', end='')
		print('')
	
# find all possible moves
def find_moves(colour, board):
	moves = []

	if colour == black:
		opponent = white
	else:
		opponent = black
	
	for i in range(8):
		for j in range(8):
			tile = int(str(i) + str(j))

			# check if current players piece is in tile
			if board.gameBoard[tile] == colour:

				# check each direction for adjacent opponent tiles
				for pos in adjacents:

					# if opponent in adjacent tile, check next tiles in that direction
					if board.gameBoard[tile + pos] == opponent:
						next = tile + pos

						while board.gameBoard[next + pos] == opponent:
							next += pos
					
						# make sure loop didnt reach the border
						if board.gameBoard[next + pos] == empty:
							if (next + pos) not in moves:
								moves += [next + pos]
	
	return moves

# alter the board based on a move made,
# assumes "move" param is legal
def update_board(colour, board, move):
	if colour == black:
		opponent = white
	else:
		opponent = black

	# Make the actual move (before flipping)
	board.gameBoard[move] = colour

	# Copy of move so we can reset it each loop
	pos = move

	# Flip pieces
	for dir in adjacents:
		pos = move

		# There is at least one opponent piece this direction
		if board.gameBoard[pos + dir] == opponent:
			# Move in that direction once (pseudo do-while loop)
			pos = pos + dir

			# Keep going while we still see opponent pieces
			while board.gameBoard[pos] == opponent:
				pos = pos + dir

			# We hit another one of our pieces, this direction requires flipping
			if board.gameBoard[pos] == colour:

				# Go back down the line in reverse and flip opponent pices
				while board.gameBoard[pos - dir] == opponent:
					if(colour == black):
						board.white_pieces += 1
					else:
						board.black_pieces += 1
					pos = pos - dir
					board.gameBoard[pos] = colour
	
	return board.gameBoard

def choose_move(colour, moves):
	# ai move
	if colour == ai:
		# implement heuristic
		pass # temporarily prevent syntax error for else statement
		
	# player move
	else:
		move = int(input(">> "))
	return move

class OthelloGame:
	gameBoard = [empty] * 100
	black_pieces = 30
	white_pieces = 30

	def __init__(self):
		# init method

		global ai
		
		# set border pieces to "border"
		for i in range(100):
			if i < 10 or i > 89 or i % 10 == 0 or i % 10 == 9:
				self.gameBoard[i] = border
		# set 44 and 55 to "white"
		self.gameBoard[44] = white
		self.gameBoard[55] = white

		# set 54 and 45 to "black"
		self.gameBoard[54] = black
		self.gameBoard[45] = black

		# randomly select colour AI
		colours = [black, white]
		ai = choice(colours)
		if ai == black:
			you = white
		else:
			you = black
		print("You are " + you + ", B's turn is first")

	def play_game(self):
		over = False
		active = black
		inactive = white
		while not over:
			legal_moves = find_moves(active, self)
			if len(legal_moves) == 0 and len(find_moves(inactive, self)) == 0:
				over = True
				continue
			if len(legal_moves) == 0:
				print("No legal moves for " + active + ", skipping their turn.")
				temp = active
				active = inactive
				inactive = temp
			show_board(self)
			print(active + "'s turn. Choose a move from " + str(legal_moves))

			move = choose_move(active, legal_moves) # has option for AI / Player

			print(active + " chose " + str(move) + ".")

			update_board(active, self, move)

			temp = active
			active = inactive
			inactive = temp


# main program
def main():
	game_main = OthelloGame()
	
	game_main.play_game()

main()
