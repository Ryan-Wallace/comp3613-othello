# Logan VanOostrum, Ryan Wallace, Ben McNutt
empty = '⋅'
black = 'B'
white = 'W'
border = '□'
adjacents = [-11, -10, -9, -1, +1, +9, +10, +11]

class OthelloGame:
	gameBoard = [empty] * 100
	blackPieces = 30
	whitePieces = 30

	def __init__(self):
		#init method
		
		#set border pieces to "border"
		for i in range(100):
			if i < 10 or i > 89 or i % 10 == 0 or i % 10 == 9:
				self.gameBoard[i] = border
		#set 44 and 55 to "white"
		self.gameBoard[44] = white
		self.gameBoard[55] = white

		#set 54 and 45 to "black"
		self.gameBoard[54] = black
		self.gameBoard[45] = black




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

#alter the board based on a move made
def update_board(colour, board, move):
	new_board = list(board.gameBoard)

	if colour == black:
		opponent = white
	else:
		opponent = black

	new_board[move] = colour

	pos = move

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



# main program
def main():
	game_main = OthelloGame()
	show_board(game_main)

	print(find_moves(black, game_main))

	game_main.gameBoard = update_board(black, game_main, 34)
	show_board(game_main)

main()
