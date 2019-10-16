        
def gameStart() :    
    loop = False
    while (loop == False) :
        print ('What do you want to play?')
        print ('1.) Single player')
        print ('2.) 2 Player')
        print ('3.) How to play')
        print ('Please choose number do you want')
        number = input()
        if number == '1' :
            bot = singlePlayer()
            if bot != 'Back' :
                loop = True
                return bot
        elif number == '2':
            player = '2Player'
            loop = True
            return player
        elif number == '3':
            howToPlay()
            loop == True

        
def singlePlayer() :
    print ('## Single player ##')
    print ('1.) Easy bot')
    print ('2.) Medium bot')
    print ('3.) Back to the menu')
    loop = False
    while (loop == False) :
        print ('Please choose number do you want')
        number = input()
        if number == '1' :
            bot = 'Easy'
            loop = True
            return bot
        elif number == '2' :
            bot = 'Medium'
            loop = True
            return bot
        elif number == '3':
            bot = 'Back'
            loop = True
            return bot  

def howToPlay () :
    loop = False
    while (loop == False) :
        print ('## How to play ##')
        print ('In the Quest Master game Will divide the gameplay into 3 parts')
        print ('1.) Character')
        print ('2.) Winning rules')
        print ('3.) How to play')
        print ('4.) Back to the menu')
        print ('Please choose the number you want to learn more')
        number = input()
        if number == '1' :
            print ('## Character ##')
            print ('** All characters have normal attack skill is use MP 2 for At 2 except for swordman **')
            print ('1.) ( Priest ), Priest will have HP starting at 26.\n    The skill is to use MP 2 for HP+2.\n    It will start at position P on the map (O14).')
            print ('2.) ( Swordman ), Swordman will have HP starting at 23.\n    The skill is to use MP 2 for At 3 and skill use MP 3 for At 4.\n    It will start at the position S on the map (C14)')
            print ('3.) ( Magician ), Magician will have HP starting at 24.\n    There is a skill when defending a fight. If starting a fight with MP 0, will increase MP by 2.\n    It starting at M position on the map (B3)')
            print ('4.) ( Robots ), The robot will have HP starting at 25.\n    The skill is to use MP 1 for Shield 2.\n    It will start at the F position on the map (H7)')
            print ('5.) ( Demon ), The demon will have HP starting at 23.\n    The skill is to use MP 3 for At 2 and HP+1.\n    t will start at position D on the map (O3)')
            print ('Press Enter for back to the menu')
            enter = input()
        elif number == '2' :
            print ('## Winning rules ##')
            print ('1.) Players have HP more than 40 ')
            print ('2.) The last remaining player')
            print ('3.) Players who enter all 5 of the castles')
            print ('Press Enter for back to the menu')
            enter = input()
        elif number == '3' :
            print ('## How to play ##')
            print ('1.) Players who roll two dice And then choose to walk or draw cards according to the face of the dice you get,\n    such as walking 3 and a sword. Players choose to walk 3 slots or battle')
            print ('2.) When a player falls to a different location (Place), the player must follow the specified details on that location')
            print ('3.) In the case of falling into the Item ( I ), players get 1 Item card')
            print ('4.) In the case of falling into the Event ( E ), the player draws an Event card and acts as described by the card')
            print ('5.) In case of falling into the Battle ( B ), players must choose to battle or not')
            print ('6.) In case of falling into the Warp ( W ), players can travel to other Warp spots')
            print ()
            print ('## In the battle ##')
            print ('When battle both of them must roll the dice to get their MP. The MP is used to use the Item card or the character skill.')
            print ('* Which the battle will start from *')
            print ('1.) The challenger will attack first by getting At+2 for free and can use the card only At card and AD card.\n    then use the character skill and then end turn.')
            print ('2.) The other person will be able to turn, defend and attack.\n    Which can use any card Then use the character skill and then end turn')
            print ('3.) The challenger will get a defense turn, cannot attack and can only use Df card and AD card,\n    use the character skill and then end turn.')
            print ('4.) It will conclude the battle and continue the game.')  
            print ('Press Enter for back to the menu')
            enter = input()   
        else :
            loop = True
        
        