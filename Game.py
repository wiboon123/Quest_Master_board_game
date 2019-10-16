import chooseCharacter
import Player
import swapPlayer
import printBoard
import dice
import moveCharacter
import checkBoard
import eventCard
import checkForWin
import ItemCard
import battle
import randomBot
import gameStart
import RuleBot

class Game :

    def main() :
        print("## Welcome to QuestMaster board game ##")
        print("============================================")

        deck = ItemCard.Deck()
        deck.shuffle()
        
        player2 = gameStart.gameStart()

        print("## Please choose the character you want to play ##")    
        p1 = chooseCharacter.p1_character()
        p2 = chooseCharacter.p2_character(player2)

        
        player1 = Player.Player(p1[0], p1[1], p1[2], p1[3])
        if player2 == 'Easy' :
            bot = randomBot.Bot(p2[0], p2[1], p2[2], p2[3])
        elif player2 == 'Medium' :
            bot = RuleBot.Bot(p2[0], p2[1], p2[2], p2[3])   ## Add custom bot below
        else :
            bot = Player.Player(p2[0], p2[1], p2[2], p2[3])
        print ()


        gameRunning = False
        turn = True
        eventCards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
        21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

        while (gameRunning == False) :
            print ('!! Game is running !!')
            turn, player, p2 = swapPlayer.swapTurn(turn, player1, bot)
            
            if player.status == 1 :
                player.status = player.status - 1
                print ('* * Player stop 1 turn * *')
            else :
                print ('## Show board ##')
                printBoard.board(player.position)
                walk = dice.rollTheDice(turn, player, eventCards, p2)
                if walk == 'Item' :
                    print ('get 1 item card')
                    player.draw(deck)
                elif walk == 'Event' :
                    eventCards, item = eventCard.eventCard(player, eventCards, p2, deck, turn)
                    if item == 1 :
                        player.draw(deck)
                    elif item == 2 :
                        player.draw(deck)
                        player.draw(deck)
                elif walk == 'Battle' :
                    battle.battle(player, p2, turn)
                else :
                    player.position = moveCharacter.move(player, walk)
                    check = printBoard.board(player.position)
                    eventCards = checkBoard.checkBoard(check, player, eventCards, deck, turn, player1, p2)
                if player.hand != [] :
                    print ('Do you want to show card on your hand ?')
                    print ('1. Yes')
                    print ('2. No')
                    showHand = player.showCard()
                    if showHand == 1 :
                        print ('# Your item card #')
                        player.showHand()
                        print ()

                player.checkItemcard()

            if turn == False :
                player1 = player
                bot = p2
            else :
                bot = player
                player1 = p2

            print ('Now player =', player1.character, ', HP =', player1.hp,', Enter the castle', player1.castle)
            print ('Now bot =', bot.character, ', HP =', bot.hp,', Enter the castle', bot.castle)
            end = player.endTrun()
            print ("================== End turn ======================")
            gameRunning = checkForWin.checkForWin(gameRunning, turn, player1, bot)
            

            if deck == [] :
                deck = ItemCard.Deck()
                deck.shuffle()
            print ()
    
            
    if __name__ == "__main__":
        main()

