# Logan VanOostrum, Ryan Wallace, Ben McNutt

from random import choice

empty = '⋅'
black = 'B'
white = 'W'
border = '□'
adjacents = [-11, -10, -9, -1, +1, +9, +10, +11]
weights = [0 for i in range(100)]
ai = ''
heuristic = "weighted"

for i in range(100):
	if i in [11, 81, 18, 88]:
		weights[i] = 10
	if i in [21, 12, 71, 82, 28, 17, 78, 87]:
		weights[i] = -5
	if i in [22, 72, 27, 77]:
		weights[i] = -10
	if i in [13, 16, 31, 33, 36, 38, 61, 63, 66, 68, 83, 86]:
		weights[i] = 6
	if i in [14, 15, 34, 35, 41, 43, 44, 45, 46, 48, 51, 53, 54, 55, 56, 58, 64, 65, 84, 85]:
		weights[i] = 3

# print game board
def show_board(board):
	for i in range(10):
		for j in range(10):
			print(str(board[i + (j * 10)]) + ' ', end='')
		print('')
	
# find all possible moves
def find_moves(colour, board):
	moves = []

	if colour == black:
		opponent = white
	else:
		opponent = black
	
	for i in range(1, 9):
		for j in range(1, 9):
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
def update_board(colour, board_array, move):
	if colour == black:
		opponent = white
	else:
		opponent = black

	new_board = list(board_array)

	# Make the actual move (before flipping)
	new_board[move] = colour

	# Copy of move so we can reset it each loop
	pos = move

	# Flip pieces
	for dir in adjacents:
		pos = move

		# There is at least one opponent piece this direction
		if new_board[pos + dir] == opponent:
			# Move in that direction once (pseudo do-while loop)
			pos = pos + dir

			# Keep going while we still see opponent pieces
			while new_board[pos] == opponent:
				pos = pos + dir

			# We hit another one of our pieces, this direction requires flipping
			if new_board[pos] == colour:

				# Go back down the line in reverse and flip opponent pices
				while new_board[pos - dir] == opponent:
					pos = pos - dir
					new_board[pos] = colour
	
	return new_board

def count_pieces(board_array, colour):
	count = 0
	for tile in board_array:
		if tile == colour:
			count += 1

	return count

def choose_move(colour, moves, board_array):
	# ai move
	if colour == ai or colour != ai:
		if(heuristic == "greedy"):
			pieces = 0
			for move in moves:
				future_board = update_board(colour, board_array, move)
				if count_pieces(future_board, colour) > pieces:
					chosen_move = move
					pieces = count_pieces(future_board, colour)

		if(heuristic == "weighted"):
			weight = -100
			flipped = []
			for move in moves:
				future_board = update_board(colour, board_array, move)
				for i in range(100):
					if future_board[i] != board_array[i]:
						flipped += [i]
				for pos in flipped:
					weight += weights[pos]
				if weights[move] > weight:
					chosen_move = move
					weight = weights[move]

	# player move
	else:
		chosen_move = int(input(">> "))
	return chosen_move

class OthelloGame:
	gameBoard = [empty] * 100

	def __init__(self):
		# init method

		global ai
		
		# set border pieces to respective coordinates
		for i in range(8):
			self.gameBoard[i + 1] = str(i + 1)

		for i in range(8):
			self.gameBoard[(i + 1) * 10] = str(i + 1)

		#add border on corners
		for i in [0, 9, 90, 99]:
			self.gameBoard[i] = border

		#add border on sides
		for i in range(8):
			self.gameBoard[i + 91] = border

		for i in range(8):
			self.gameBoard[((i + 1) * 10) + 9] = border
		
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
				break
			if len(legal_moves) == 0:
				print("No legal moves for " + active + ", skipping their turn.")
				temp = active
				active = inactive
				inactive = temp
			show_board(self.gameBoard)
			print(active + "'s turn. Choose a move from " + str(legal_moves))

			move = choose_move(active, legal_moves, self.gameBoard) # has option for AI / Player

			print(active + " chose " + str(move) + ".")

			self.gameBoard = update_board(active, self.gameBoard, move)

			temp = active
			active = inactive
			inactive = temp

		if count_pieces(white,self.gameBoard) > count_pieces(black,self.gameBoard):
			winner = white
		else:
			winner = black
		print("The game is over, " + winner + " wins!")
		


# main program
def main():
	game_main = OthelloGame()
	
	game_main.play_game()

main()
