"""
Basic terminal connect 4 before creating GUI version 
"""
# Imports 
import pygame

# Creating Basic Gameboard in Terminal 
def create_board(columns, rows):
	for col in range(columns): 
		print("-" * 70) 
		for row in range(rows): 
			print("{}{}".format("|", "          "))


# Main Function 
if __name__ == "__main__": 
	# Inserting Space 
	print("\n\n")
	# Passes standard gameboard columns and rows 
	create_board(7, 6)
	# Inserting Space 
	print("\n\n")