def swapTurn(turn, p1, p2) :
    if turn == True :
        print ('=============== Player 1 turn ===============')
        turn = False
        player = p1
        player2 = p2
    else :
        print ('=============== Player 2 turn ===============')
        turn = True
        player = p2
        player2 = p1
    return turn, player, player2