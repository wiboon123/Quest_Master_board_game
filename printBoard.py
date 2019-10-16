import checkPosition

def board(positionNow) : 
    board = [
         [" ","E","B","I","2","I","B","E","B","E"," "," "," "," "," "," "],
         [" ","I"," "," ","B"," "," "," "," ","W","B"," ","E","B","I",' '],
         [" ","M"," "," ","I","E","B","W"," "," ","E","B","I"," ","D",' '],
         [" ","E","B"," "," "," "," ","I","E","E"," "," "," "," ","B",' '],
         [" "," ","E"," ","4","I"," "," "," ","I"," "," "," ","I","E",' '],
         ["W","I","B","E","B","B"," "," "," ","E"," "," "," ","E"," ",' '],
         ["E"," "," "," "," ","I","E","F","B","I"," "," "," ","I"," ",' '],
         ["E","1","B"," "," "," "," "," "," "," "," "," ","E","B"," ",' '],
         [" "," ","E","B","I","E","W"," "," "," "," "," ","B"," "," ",' '],
         [" "," "," "," "," "," ","B"," "," "," "," "," ","I"," "," ",' '],
         ["I","I","B","E","B","E","I"," "," "," "," "," ","3","B","I",'B'],
         ["E"," "," "," "," "," "," "," "," "," "," "," "," "," "," ",'W'],
         ["B"," "," "," "," "," "," "," "," "," "," "," "," "," "," ",'E'],
         ["I","E","S","I","E","I","E","B","I","B","E","4","E","B","P",'I']
        ]
    print('   A B C D E F G H I J K L M N O P')
    number = 0
    for i in board:
        number = number + 1
        if number < 10 :
            print(str(number) + '  ', end='')
        else :
            print(str(number) + ' ', end='')
        for cell in i:
            print(cell,end = " ")
        print()
    position = [
        [board[13][0]], [board[13][1]], [board[13][2]], [board[13][3]], [board[13][4]],
        [board[13][5]], [board[13][6]], [board[13][7]], [board[13][8]], [board[13][9]],
        [board[13][10]], [board[13][11]], [board[13][12]], [board[13][13]], [board[13][14]],
        [board[13][15]], [board[12][15]], [board[11][15]], [board[10][15]], [board[10][14]],
        [board[10][13]], [board[10][12]], [board[9][12]], [board[8][12]], [board[7][12]],
        [board[7][13]], [board[6][13]], [board[5][13]], [board[4][13]], [board[4][14]],
        [board[3][14]], [board[2][14]], [board[1][14]], [board[1][13]], [board[1][12]],
        [board[2][12]], [board[2][11]], [board[2][10]], [board[1][10]], [board[1][9]],
        [board[0][9]], [board[0][8]], [board[0][7]], [board[0][6]], [board[0][5]],
        [board[0][4]], [board[0][3]], [board[0][2]], [board[0][1]], [board[1][1]],
        [board[2][1]], [board[3][1]], [board[3][2]], [board[4][2]], [board[5][2]],
        [board[5][1]], [board[5][0]], [board[6][0]], [board[7][0]], [board[7][1]],
        [board[7][2]], [board[8][2]], [board[8][3]], [board[8][4]], [board[8][5]],
        [board[8][6]], [board[9][6]], [board[10][6]], [board[10][5]], [board[10][4]],
        [board[10][3]], [board[10][2]], [board[10][1]], [board[10][0]], [board[11][0]],
        [board[12][0]], [board[5][3]], [board[5][4]], [board[4][4]], [board[4][5]],
        [board[5][5]], [board[6][5]], [board[6][6]], [board[6][7]], [board[6][8]],
        [board[6][9]], [board[5][9]], [board[4][9]], [board[3][9]], [board[3][8]],
        [board[3][7]], [board[2][7]], [board[2][6]], [board[2][5]], [board[2][4]],
        [board[1][4]],
    ]
    playerPosition = positionNow
    checkPosition.checkPosition(playerPosition, position[playerPosition])
    return playerPosition, position[playerPosition]