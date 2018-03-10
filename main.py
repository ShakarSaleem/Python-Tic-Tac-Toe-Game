from gameboardfixed_st import GameBoardFixed
from player_st import Player


def main():

	gboard = GameBoardFixed(3)
	
	p1 = Player("X", gboard)	# create player 1 object
	p2 = Player("O", gboard)	# create player 2 object
	
	# place players 1 and 2 in tuple for turn based game. 
	players_lst = (p1, p2)
	
	winner = False
	
	gboard.show_board_fixed() # show empty grid at the beginning of the game
	
	while (winner == False):
		# This is to allow players to take turns. 
		# The game begins with the player at index zero in the tuple,
		# When the player completes its turn, the next player in the tuple will be asked to play. 
		# If there is no winner, this continue until reaching the end of the players list, and then we start again
		# from teh begging of the list.
		
		for p in players_lst:
			p.play()
			gboard.show_board_fixed() # After each move, the board is shown on the screen
			winner = gboard.check_winner() # The board will check after each move, if any player has won the game
			
			if winner == True:
				# Show current player's symbol as Winner, 
				# and terminate the game
				print()
				print ("Player %s is the Winner!" % p.get_player_symbol())
				break  # end the game and announce the winner.
							
main()		
