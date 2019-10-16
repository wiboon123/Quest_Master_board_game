import Player
import randomBot

def checkForWin(game, turn, p1, p2) :
    if p1.hp >= 40 :
        p1win()
        game = True
    elif p2.hp >= 40 :
        p2win()
        game = True
    elif p1.hp <= 0 :
        p2win()    
        game = True
    elif p2.hp <= 0 :
        p1win()
        game = True
    else :
       castle = checkCastle(turn, p1, p2, game)
       if castle == True :
           game = True
    return game

def checkCastle (turn ,p1, p2, game) :
    if turn == False :
        if len(p1.castle) == 5 :
            p1win()
            game = True
    else :
        if len(p2.castle) == 5 :
            p2win()
            game = True
    return game
        

def p1win () :
    print ('==================================================')
    print ('==                                              ==')
    print ('==  ||||||    ||    ||      ||  ||  ||      ||  ==')
    print ('==  ||  ||  ||||    ||      ||      ||||    ||  ==')
    print ('==  ||||||    ||    ||  ||  ||  ||  ||  ||  ||  ==')
    print ('==  ||        ||    ||||  ||||  ||  ||    ||||  ==')
    print ('==  ||      ||||||  ||      ||  ||  ||      ||  ==')
    print ('==                                              ==')
    print ('==================================================')
    print ('==================================================')
    
def p2win() :
    print ('==================================================')
    print ('==                                              ==')
    print ('==  ||||||  ||||||  ||      ||  ||  ||      ||  ==')
    print ('==  ||  ||      ||  ||      ||      ||||    ||  ==')
    print ('==  ||||||    ||    ||  ||  ||  ||  ||  ||  ||  ==')
    print ('==  ||      ||      ||||  ||||  ||  ||    ||||  ==')
    print ('==  ||      ||||||  ||      ||  ||  ||      ||  ==')
    print ('==                                              ==')
    print ('==================================================')
    print ('==================================================')
