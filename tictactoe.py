# This program allows you to play Tic Tac Toe with your friend!
# Program created by: Jeferson A. Tadios

gameboard = ["☐", "☐", "☐",
         "☐", "☐", "☐",
         "☐", "☐", "☐"]

get_player1 = input("Enter Player 1's Name: ")
get_player2 = input("Enter Player 2's Name: ")

player_turn = {
    "Name":get_player1,
    "Symbol":"X"
}

def board_preview():
    print("\n"
    +gameboard[0]+" "+gameboard[1]+" "+gameboard[2]+"\n"
    +gameboard[3]+" "+gameboard[4]+" "+gameboard[5]+"\n"
    +gameboard[6]+" "+gameboard[7]+" "+gameboard[8]+"\n"
    +"\n")

board_preview()
print(player_turn["Name"]+"'s Turn")
pos = input("Choose a position from 0-9: ")
print(pos)


