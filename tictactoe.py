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
    +gameboard[0]+"  | "+gameboard[1]+"  | "+gameboard[2]+"    1 | 2 | 3"+"\n"
    +gameboard[3]+"  | "+gameboard[4]+"  | "+gameboard[5]+"    4 | 5 | 6"+"\n"
    +gameboard[6]+"  | "+gameboard[7]+"  | "+gameboard[8]+"    7 | 8 | 9"+"\n"
    +"\n")

def choose_position():
    print(player_turn["Name"]+"'s Turn")
    pos = (input("Choose a position from 1-9: "))
    filled = False
    while filled != True:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("Choose a position from 1-9: ")
        pos = int(pos) - 1
        if gameboard[pos] == "☐":
            filled = True
        else:
            print("Position is already filled! Please choose another position")
    gameboard[pos] = player_turn["Symbol"]
    board_preview()


def change_player():
    if player_turn["Symbol"] == "X":
        player_turn["Symbol"] = "O"    
    elif player_turn["Symbol"] == "O":
        player_turn["Symbol"] = "X"
    if player_turn["Name"] == get_player1:
        player_turn["Name"] = get_player2    
    elif player_turn["Name"] == get_player2:
        player_turn["Name"] = get_player1


def row_winner():
    row1 = gameboard[0] == gameboard[1] == gameboard[2] != "☐"
    row2 = gameboard[3] == gameboard[4] == gameboard[5] != "☐"
    row3 = gameboard[6] == gameboard[7] == gameboard[8] != "☐"
    if row1:
        winner = gameboard[0]
        if winner == "X":
            print(get_player1 + " won.")
        elif winner == "O":
            print(get_player2 + " won.")
        exit()
    elif row2:
        winner = gameboard[3]
        if winner == "X":
            print(get_player1 + " won.")
        elif winner == "O":
            print(get_player2 + " won.")
        exit()
    elif row3:
        winner = gameboard[6]
        if winner == "X":
            print(get_player1 + " won.")
        elif winner == "O":
            print(get_player2 + " won.")
        exit()


board_preview()
while True:
    choose_position()
    change_player()
    row_winner()
    if "☐" not in gameboard:
        print("Game Ended with a tie!")
        exit()


    


