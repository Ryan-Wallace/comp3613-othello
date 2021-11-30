# Logan VanOostrum, Ryan Wallace, Ben McNutt
empty = '*'
black = 'B'
white = 'W'
border = '='

class OthelloGame:
	gameBoard = [empty] * 100
	blackPieces = 30
	whitePieces = 30

	def __init__(self):
		#init method
		
		#set border pieces to "border"

		#set 44 and 55 to "white"

		#set 54 and 45 to "black"

		return

# print game board
def show_board(board):
	for i in range(10):
		for j in range(10):
			print(board.gameBoard[(i * 10) + j], end='')
		print('')

# find all possible moves
def find_moves(colour, board):
	moves = []
	adjacents = [-11, -10, -9, -1, +1, +9, +10, +11]

	if colour == 'B':
		opponent = 'W'
	else:
		opponent = 'B'
	
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
						if board.gameBoard[next + pos] == '*':
							if (next + pos) not in moves:
								moves += [next + pos]
	
	return moves









# main program
def main():
	game_main = OthelloGame()
	show_board(game_main)