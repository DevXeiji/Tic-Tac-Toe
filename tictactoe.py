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
    +gameboard[0]+"  | "+gameboard[1]+"  | "+gameboard[2]+"    0 | 1 | 2"+"\n"
    +gameboard[3]+"  | "+gameboard[4]+"  | "+gameboard[5]+"    3 | 4 | 5"+"\n"
    +gameboard[6]+"  | "+gameboard[7]+"  | "+gameboard[8]+"    6 | 7 | 8"+"\n"
    +"\n")

def choose_position():
    print(player_turn["Name"]+"'s Turn")
    pos = input("Choose a position from 0-9: ")
    pos = int(pos)
    gameboard[pos] = player_turn["Symbol"]
    board_preview()

board_preview()
choose_position()


if player_turn["Symbol"] == "X":
    player_turn["Symbol"] = "O"    
elif player_turn["Symbol"] == "O":
    player_turn["Symbol"] = "X"  
print(player_turn["Symbol"])


