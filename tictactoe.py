# This program allows you to play Tic Tac Toe with your friend!
# Program created by: Jeferson A. Tadios

gameboard = ["☐", "☐", "☐",
         "☐", "☐", "☐",
         "☐", "☐", "☐"]

get_player1 = input("Enter Player 1's Name: ")
get_player1symbol = input("Enter Player 1's desired Symbol: ")
get_player2 = input("Enter Player 2's Name: ")
get_player2symbol = input("Enter Player 1's desired Symbol: ")

player_turn = {
    "Name":get_player1,
    "Symbol":get_player1symbol
}

def board_preview():
    for i in enumerate(gameboard):
        if i[0] == 0:
            p1 = "[1]" if i[1] == "☐" else gameboard[0]
        if i[0] == 1:
            p2 = "[2]" if i[1] == "☐" else gameboard[1]
        if i[0] == 2:
            p3 = "[3]" if i[1] == "☐" else gameboard[2]
        if i[0] == 3:
            p4 = "[4]" if i[1] == "☐" else gameboard[3]
        if i[0] == 4:
            p5 = "[5]" if i[1] == "☐" else gameboard[4]
        if i[0] == 5:
            p6 = "[6]" if i[1] == "☐" else gameboard[5]
        if i[0] == 6:
            p7 = "[7]" if i[1] == "☐" else gameboard[6]
        if i[0] == 7:
            p8 = "[8]" if i[1] == "☐" else gameboard[7]
        if i[0] == 8:
            p9 = "[9]" if i[1] == "☐" else gameboard[8]
    print(p1 + " | " + p2 + " | " + p3)
    print(p4 + " | " + p5 + " | " + p6)
    print(p7 + " | " + p8 + " | " + p9)

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
    if player_turn["Symbol"] == get_player1symbol:
        player_turn["Symbol"] = get_player2symbol    
    elif player_turn["Symbol"] == get_player2symbol:
        player_turn["Symbol"] = get_player1symbol
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
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()
    elif row2:
        winner = gameboard[3]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()
    elif row3:
        winner = gameboard[6]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()

def diagonal_winner():
    diagonal1 = gameboard[0] == gameboard[4] == gameboard[8] != "☐"
    diagonal2 = gameboard[2] == gameboard[4] == gameboard[6] != "☐"
    if diagonal1:
        winner = gameboard[0]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()
    elif diagonal2:
        winner = gameboard[2]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()


def vertical_winner():
    vertical1 = gameboard[0] == gameboard[3] == gameboard[6] != "☐"
    vertical2 = gameboard[1] == gameboard[4] == gameboard[7] != "☐"
    vertical3 = gameboard[2] == gameboard[5] == gameboard[8] != "☐"
    if vertical1:
        winner = gameboard[0]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()
    elif vertical2:
        winner = gameboard[1]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()
    elif vertical3:
        winner = gameboard[2]
        if winner == get_player1symbol:
            print(get_player1 + " won.")
        elif winner == get_player2symbol:
            print(get_player2 + " won.")
        exit()


board_preview()
while True:
    choose_position()
    change_player()
    row_winner()
    diagonal_winner()
    vertical_winner()
    if "☐" not in gameboard:
        print("Game Ended with a tie!")
        exit()
    

    


