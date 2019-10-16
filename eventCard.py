import random
import printBoard
import checkBoard
import ItemCard
import battle
import Player
import randomBot
import RuleBot



def eventCard(player, cards, enemy, deck, turn) :
    item = 0
    eventCards = random.choice(cards)
    cards.remove(eventCards) 
    if cards == [] :
        for i in range(36) :
            cards.append(i + 1)

    print ("## Event card ##")
    if eventCards == 1 :
        print ("Found the mother and baby bear")
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if  red == "Battle":
            print ('Bitten')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
        else :
            print ('Friendly')
            print ('get 1 item card')
            item = 1
    elif eventCards == 2 :
        print ('Found lord vampire')
        if player.character == "Priest" :
            print ('Win')
            print ('get 1 item card') 
            item = 1
        elif player == "Demon":
            print ('Increase power')
            player.hp = player.hp + 3
            print ('Player Hp + 3 =', player.hp)
        elif player.character == "Swordman" or player.character == "Magician" :
            print ('Sucked blood')
            player.hp = player.hp - 2
            print ('Player Hp - 2 = ', player.hp)
        else:
            print ('Nothing happened')
    elif eventCards == 3 :
        print ('This is something')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == "Battle" :
            print ('It is a bomb')
            player.hp = player.hp - 3
            print ('Player Hp - 3 = ', player.hp)
        else :
            print ('It was crab and clamped into it')
            player.hp = player.hp - 1
            print ('Player Hp - 1 = ', player.hp)
    elif eventCards == 4 :
        print ('Found a strange tribe')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == "Battle" :
            print ('Shy tribe fled')
            print ('Nothing happened')
        else :
            print ('Provide accommodation')
            print ('Stop 1 turn')
            player.status = player.status + 1
    elif eventCards == 5 :
        print ('Found a ferocious lizard')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == "Battle" :
            print ('win')
            print ('get 1 item card')
            item = 1
        else :
            print ('Attacked')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
    elif eventCards == 6 :
        print ('Fishing can be a dragon')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == "Battle" :
            print ('Dragon Attack')
            player.hp = player.hp - 3
            print ('Player HP - 3 = ', player.hp)
        else :
            print ('Dragon brought the goods to')
            print ('get 1 item card') 
            item = 1
    elif eventCards == 7 :
        print ('Walking into the abyss.')
        player.hp = player.hp - 3
        print ('Player HP - 3 = ', player.hp)
        print ('Stop 1 turn')
        player.status = player.status + 1
    elif eventCards == 8 :
        print ('Take a bath onsen')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            player.hp = player.hp + 1
            print ('Player HP + 1 = ', player.hp)
        else :
            print ('Player HP increase according to the number of pitches')
            player.hp = player.hp + red
            print ('Player Hp +', red ,'= ', player.hp)
    elif eventCards == 9 :
        print ('Angel appeared')
        if player.character == "Priest" :
            print ('Received')
            print ('get 1 item card') 
            item = 1
        elif player.character == "Demon" :
            print ('Lost to the sacred')
            player.hp = player.hp - 2 
            print ('Player HP - 2 = ', player.hp) 
        else :
            print ('blessed')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
    elif eventCards == 10 :
        print ('Meet bird nurse')
        player.hp = player.hp + 4
        print ('Player HP + 4 = ', player.hp)
    elif eventCards == 11 :
        print ('Meet nuns')
        if player.character == 'Demon' :
            print ('Repent')
            print ('Stop 1 turn')
        else :
            redDice = [1,2,3,4,"Battle","Battle"]
            red = random.choice(redDice)
            print ("The red dice is ", red)
            if red == 'Battle' :
                print ('Nuns point the way')
                print ('Go to the church')
                player.position = 14
                checkBoard.priestCastle(player)
            else :
                print ('The nun breaks the dessert')
                player.hp = player.hp + 3
                print ('Player HP + 3 = ', player.hp)
    elif eventCards == 12 :
        print ('Found flowers rushing to sniff')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Bitten by the head')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
        else :
            print ('fragrance')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
    elif eventCards == 13 :
        print ('Hungry & faint')
        player.hp = player.hp - 1
        print ('Player HP - 1 and stop 1 turn', player.hp)
        print ('Stop 1 turn')
        player.status = player.status + 1
    elif eventCards == 14 :
        print ('Find the goddess')
        print ('Choose one')
        print ('1. get 1 item card')
        print ('2. HP + 3')
        choose = player.detailEvent(eventCards)
        if choose == 1 :
            print ('get 1 item card')
            item = 1
        else :
            player.hp = player.hp + 3
            print ('Player HP + 3', player.hp)
    elif eventCards == 15 :
        print ('Mole dig out something')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Get a bomb')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
        else :
            print ('Get a item')
            item = 1
    elif eventCards == 16 :
        print ('Find a mage')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            if player.character == 'Magician' :
                player.hp = player.hp + 3
                print ('Player HP + 3 = ', player.hp)
            else :
                print ('guide')
                print ('go to magic School')
                player.position = 50
                checkBoard.magicSchool(player, enemy, deck)
        else :
            print ('give item')
            print ('get 1 item card') 
            item = 1
    elif eventCards == 17 :
        print ('Found a sacred pond')
        if player.hp > 15 :
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
        else :
            player.hp = player.hp + 4
            print ('Player HP + 4 = ', player.hp)
    elif eventCards == 18 :
        print ('Met Medusa')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Win')
            print ('get 1 item card') 
            item = 1
        else :
            print ('petrify')
            print ('Stop 1 turn')
            player.status = player.status + 1
    elif eventCards == 19 :
        print ('Hit by a trap')
        print ('choose one')
        print ('1. Stop 1 turn')
        print ('2. Hp - 2')
        choose = player.detailEvent(eventCards)
        if choose ==  1 :
            print ('Stop 1 turn')
            player.status = player.status + 1
        else :
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
    elif eventCards == 20 :
        print ('Giant mushroom')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Poisonous mushroom')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
        else :
            print ('Edible mushrooms')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
    elif eventCards == 21 :
        print ('Find mushrooms')
        if player.character == 'Demon' :
            print ('Eat mushrooms')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
        elif player.character == 'Robot' :
            print ('Collect mushrooms')
            print ('get 1 item card')
            item = 1
        else :
            print ('Eat mushrooms')
            player.hp = player.hp + 3
            print ('Player HP + 3 = ', player.hp)
    elif eventCards == 22 :
        print ('Found an ugly mummy')
        if player.character == 'Demon' :
            print ('get 1 item card')
            item = 1
        else :
            print ('Attacked')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
    elif eventCards == 23 :
        print ('Take a nap & rest')
        player.hp = player.hp + 4
        player.status = player.status + 1
        print ('Stop 1 turn and HP + 4 =', player.hp)
    elif eventCards == 24 :
        print ('Find a scientist')
        if player.character == 'Robot' : 
            print ('Be repaired')
            player.hp = player.hp + 2
            print ('Player HP + 2 and get 1 item card', player.hp)
        else :
            print ('get 1 item card')
            item = 1
    elif eventCards == 25 :
        print ('Find a robot')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            if player.character == 'Robot' :
                print ('Player hp + 3 && get 1 item card')
                player.hp = player.hp + 3
                item = 1
            else :
                print ('get 1 item card')
                player.hp = player.hp + 3
                item = 1
                print ('Player HP + 3', player.hp)
        else :
            print ('guide')
            print ('go to Factory')
            player.position = 31
            checkBoard.factoryCastle(player, deck)
    elif eventCards == 26 :
        print ('Into the mysterious forest')
        redDice = [1,2,3,4,"Battle","Battle"] 
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Wandering the forest')
            print ('Stop 1 turn')
            player.status = player.status + 1
        else :
            print ('Found a special fruit')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
    elif eventCards == 27 :
        print ('Found a warrior carrying a flag')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Battle')
            battle.battle(player, enemy, turn)
        else :
            if player.character == 'Swordman' :
                player.hp = player.hp + red
                print ('Player HP increase according to the number of pitches')
                print ('Player Hp =', player.hp)
            else :
                print ('guide')
                player.position = 2
                checkBoard.swordCastle(player, deck)
    elif eventCards == 28 :
        print ('Meet the water goddess')
        print ('Give power')
        player.hp = player.hp + 3
        print ('Player HP + 3 = ', player.hp)
    elif eventCards == 29 :
        print ('The swarm of bees fly')
        print ('Collect honey for sale')
        print ('get 1 item card, but hit by a bee sting') 
        player.hp = player.hp - 2
        item = 1
        print ('Player HP - 2 = ', player.hp)
    elif eventCards == 30 :
        print ('Meet the Black Magician')
        print ('Attacked')
        player.hp = player.hp - 3
        print ('Player HP - 3 = ', player.hp)
    elif eventCards == 31 :
        print ('Lightning storm')
        if player.character == 'Robot' :
            print ('Get power')
            player.hp = player.hp + 3
            print ('Player HP + 3 = ', player.hp)
        else :
            print ('get hurt')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
    elif eventCards == 32 :
        print ('Dragon watching eggs')
        redDice = [1,2,3,4,"Battle","Battle"]
        red = random.choice(redDice)
        print ("The red dice is ", red)
        if red == 'Battle' :
            print ('Dunhuang dragon attack eggs')
            player.hp = player.hp - 2
            print ('Player HP - 2 = ', player.hp)
        else :
            print ('The dragon gave the eggs, get 1 item card')
            item = 1
    elif eventCards == 33 :
        print ('Beautiful girl in the forest')
        blueDice = [1,2,3,4,"Item","Event"]
        blue = random.choice(blueDice)
        print ("The blue dice is ", blue)
        if blue == 'Item' :
            print ('She is the queen giving gifts')
            print ('get 1 item card')
            item = 1
        elif blue == 'Event' :
            print ('She is a magic witch attacked')
            player.hp = player.hp - 4
            print ('Player HP - 4 = ', player.hp)
        else :
            print ('She is the angel to bless')
            player.hp = player.hp + 2
            print ('Player HP + 2 = ', player.hp)
    elif eventCards == 34 :
        print ('Weapon shop')
        blueDice = [1,2,3,4,"Item","Event"]
        blue = random.choice(blueDice)
        print ("The blue dice is ", blue)
        if blue == 'Item' :
            print ('buy 1 get 1 free')
            item = 2
        elif blue == 'Event' :
            print ('Do damage')
            print ('remove 1 item card')
            player.disCard()
        else :
            print ('Shopping')
            print ('get 1 item card')
            item = 1
    elif eventCards == 35 :
        print ('Found the sea lion king')
        blueDice = [1,2,3,4,"Item","Event"]
        blue = random.choice(blueDice)
        print ("The blue dice is ", blue)
        if blue == 'Item' :
            print ('Give 2 item')
            print ('get 2 item card') 
            item = 2
        elif blue == 'Event' :
            print ('Organize a celebration')
            player.hp = player.hp + 5
            print ('Player HP + 5 = ', player.hp)
        else :
            print ('get 1 item card')
            item = 1
    elif eventCards == 36 :
        blueDice = [1,2,3,4,"Item","Event"]
        blue = random.choice(blueDice)
        print ("The blue dice is ", blue)
        if blue == 'Item' :
            print ('Collect treasures')
            print ('get 2 item card')
            item = 2
        elif blue == 'Event' :
            print ('Is a trap')
            player.hp = player.hp - 3
            print ('Player HP - 3 = ', player.hp)
        else :
            print ('Just an illusion') 
            print ('Nothing happened')
    print ('-------------------------------------')
    return cards, item