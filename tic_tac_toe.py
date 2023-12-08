def check_board(myboard):
    store = []
    for x in myboard:
        for y in x:
            if y == 'X':
                store.append(y)
            if len(store) == 9:
                return 0
def game_over(myboard):
    #myboard = [myboard[0][0], myboard[0][1], myboard[0][2]]
    for i in range(3):
        if myboard[i][0] == myboard[i][1] == myboard[i][2]:
            return myboard[i][0] # row winner
        if myboard[0][i] == myboard[1][i] == myboard[2][i]:
            return myboard[0][i] # column winner
        if myboard[0][0] == myboard[1][1] == myboard[2][2]:
            return myboard[0][0] # diagonal winner
        if myboard[0][2] == myboard[1][1] == myboard[2][0]:
            return myboard[0][2] # anti diagonal winner
def convertToSlot():
    slot = int(input("Enter a slot numver 1 - 9: >>> "))
    slotMap = {1 : (0, 0),
               2 : (0, 1),
               3 : (0, 2),
               4 : (1, 0),
               5 : (1, 1),
               6 : (1, 2),
               7 : (2, 0),
               8 : (2, 1),
               9 : (2, 2)}
    value = slotMap[slot]
    return value

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

player2 = "O"
player1 = "X"
player1_name = input("Player 1 Enter your name : ")
player2_name = input("Player 2 Enter your name : ")
player1_point = 0
player2_point = 0
turn = player1
row = 0
column = 0
while check_board(board) != 0:
    print(f"        {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" " * 5,"-" * 10)
    print(f"        {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" " * 5,"-" * 10)
    print(f"        {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(" " * 5,"-" * 10)
    row, column = convertToSlot()
    if turn == player1:
        board[row][column] = player1
        turn = player2
    else:
        board[row][column] = player2
        turn = player1

    
    check_board(board)
    game_over(board)
    if game_over(board) == player1:
        print("\nGame Over: ", player1_name, " Win \n\n")
        print("Good Game!, Better Luck next time Mr ", player2_name)
        print("\n\n")
        break
    elif game_over(board) == player2:
        print("\nGame Over: ", player2_name, " Win")
        print("Good Game!, Better Luck next time Mr ", player1_name)
        print("\n\n")
        break
