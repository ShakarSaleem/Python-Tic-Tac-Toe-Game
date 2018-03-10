class GameBoardFixed:
	
	def __init__(self, s):
			self.__space = ' '
			size = 3
			self.__board =  []
			
			for i in range (size):
				row = [' ']*size
				self.__board.append(row)

			
	def make_move(self, row, col, element):
		self.__board[row][col] = element
		
		
	def check_winner(self):
	    # Given a board and a player's letter, this function returns True if  player has won.
		winner = ((self.__board[0][0] == self.__board[0][1] and  self.__board[0][1] == self.__board[0][2] and self.__board[0][2] != self.__space) or # check across the top
		(self.__board[1][0] == self.__board[1][1] and self.__board[1][1] == self.__board[1][2] and self.__board[1][2] != self.__space) or # check across the middle row
		(self.__board[2][0] == self.__board[2][1] and self.__board[2][1] == self.__board[2][2] and self.__board[2][2] != self.__space) or # check the bottom row
		(self.__board[0][0] == self.__board[1][0] and self.__board[1][0] == self.__board[2][0] and self.__board[2][0] != self.__space) or # check down the left side
		(self.__board[0][1] == self.__board[1][1] and self.__board[1][1] == self.__board[2][1] and self.__board[2][1] != self.__space) or # check down the middle column
		(self.__board[0][2] == self.__board[1][2] and self.__board[1][2] == self.__board[2][2] and self.__board[2][2] != self.__space) or # check down the right side
		(self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2] and self.__board[2][2] != self.__space) or # check diagonal row top left to bottom right
		(self.__board[2][0] == self.__board[1][1] and self.__board[1][1] == self.__board[0][2] and self.__board[0][2] != self.__space)) # check diagonal row top right to bottom left 
		# when performing the check, and if there are three elements are equal, then make sure they are not equal to empty space ' ' which is what the 2D array was populated with at the start of the application.
		return winner
		
	def is_board_full(self):
	    # TODO: Return True if every space on the board has been taken. Otherwise return False.
		return True
		
	def is_space_free (self, row, col):
		# TODO: Return true if the passed move is free on the passed board.
		#return True
		return True


	def show_board_dynamic(self):
		for i in range (len(self.__board)):
			for j in range (len(self.__board)):
				print (",", end = "")
				print (self.__board[i][j], end=""),
			print (",", end = "")
			print ("")
	
	# This function prints out the board that it was passed.  "board" is a list of 10 strings representing the board (ignore index 0)
	def show_board_fixed(self):
		print('   |   |')
		print(' ' + self.__board[0][0] + ' | ' + self.__board[0][1] + ' | ' + self.__board[0][2])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.__board[1][0] + ' | ' + self.__board[1][1] + ' | ' + self.__board[1][2])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.__board[2][0] + ' | ' + self.__board[2][1] + ' | ' + self.__board[2][2])
		print('   |   |')	
