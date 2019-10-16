import random
import ItemCard
import Player
import randomBot

def normalAttack(mp, damage, loop, player):
    print ('Do you want to use 2 Mp for at + 2 ?')
    print ('1.Yes')
    print ('2.No')
    chooseAttack = player.chooseNormalAttack(mp)
    if chooseAttack == 1 :
        mp = mp - 2 
        damage = damage + 2
    else :
        print ('Not attack')
        loop = True
    return mp, damage, loop

def battle(player, player2, turn) :
    print ('## Roll the dice ##')
    print ('Please enter to dice')
    enter = player.enter()
    redDice = [1,2,3,4,"Battle","Battle"]
    red = random.choice(redDice)
    print ('----------------------------------')
    if red == 'Battle' :
        p1_mp = 0
        print ("[ Player1 Mp is ",0 ,']')
    else :
        p1_mp = red
        print ('[ Player1 Mp is ', red,']')

    blueDice = [1,2,3,4,"Item","Event"]
    blue = random.choice(blueDice)
    if blue == 'Item' or blue == 'Event' :
        if player2.character == 'Magician' :
            print ('Passive skill activated change Mp 0 to 2')
            print ("[ Player2 Mp is ",2,']')
            p2_mp = 2
        else :
            p2_mp = 0
            print ("[ Player2 Mp is ",0,']')
    else :
        p2_mp = blue
        print ('[ Player2 Mp is ', blue,']')

    print ('----------------------------------')
    print ()
    print ('## Start Battle ##')
    print ('## Player1 attack turn ##')
    print ('- Player1 is a', player.character)
    print ('- Player1 Mp =', p1_mp)
    p1_damage = 2
    p2_damage = 0

    loop = False
    while (loop == False) :
        if player.hand == [] :
            loop = True
            print ()
            print ('- No card to use')
            print ()
        else :
            checkCard = False
            while (checkCard == False) :
                if player.hand == [] :
                    checkCard = True
                    loop = True
                else :
                    print ('Now player1 Mp =', p1_mp)
                    print ()
                    player.showHand()
                    print ()
                    print ('You have', len(player.hand), 'card')
                    print ('Input number to use item card & q to do not use card')
                    chooseCard = player.chooseAttackCard(p1_mp, player2)
                    if chooseCard == 'q' or chooseCard == '':
                        print ('- Do not use card')
                        checkCard = True
                        loop = True
                    else :
                        chooseCard = int(chooseCard)
                        if chooseCard > len(player.hand) :
                            print ('You have', len(player.hand), 'card')
                        else :
                            chooseCard = chooseCard - 1
                            p1_mp = p1_mp - player.hand[chooseCard].mp
                            if p1_mp < 0 :
                                p1_mp = p1_mp + player.hand[chooseCard].mp
                                print ('# Can not use the card #')
                            else :
                                print ('Use the card')
                                print ('Now p1_mp is', p1_mp)
                                detail = player.hand[chooseCard].detail.split('+')
                                if detail[0] == 'At' :
                                    p1_damage = p1_damage + int(detail[1])
                                    print ('Now damage is', p1_damage)
                                    player.hand.remove(player.hand[chooseCard])
                                elif detail[0] == 'Hp' :
                                    player.hp = player.hp + int(detail[1])
                                    player.hand.remove(player.hand[chooseCard])
                                    print ('Now player1 hp =', player.hp )
                                elif detail[0] == 'Mp' :
                                    p1_mp = p1_mp + int(detail[1])
                                    player.hand.remove(player.hand[chooseCard])
                                    print ('Now player Mp =', p1_mp)
                                elif detail[0] == 'Shield' :
                                    print ('Can not use card')

    if p1_mp >= 2 :
        attackTurn = False
        while (attackTurn == False) :
            print ('- Player1 is a', player.character)
            print ('Now player1 mp =', p1_mp)
            print ()
            if player.character == 'Swordman' :
                if p1_mp > 2 :
                    print ('Do you want to use 3 Mp for at + 4 ?')
                    print ('1.Yes')
                    print ('2.No')
                    useSkill = player.useSkill(p1_mp)
                    if useSkill == '1' :
                        p1_mp = p1_mp - 3
                        p1_damage = p1_damage + 4
                        print ('Now player1 mp =', p1_mp)
                        print ('Player1 damage =', p1_damage)
                    else :
                        print ('Do you want to use 2 Mp for at + 3 ?')
                        print ('1.Yes')
                        print ('2.No')
                        useSkill = player.useSkill(p1_mp)
                        if useSkill == '1' :
                            p1_mp = p1_mp - 2
                            p1_damage = p1_damage + 3
                            print ('Now player1 mp =', p1_mp)
                            print ('Player1 damage =', p1_damage)
                        else :
                            print ('Not attack')
                            attackTurn = True
                else :
                    print ('Do you want to use 2 Mp for at + 3 ?')
                    print ('1.Yes')
                    print ('2.No')
                    useSkill = player.useSkill(p1_mp)
                    if useSkill == '1' :
                        p1_mp = p1_mp - 2
                        p1_damage = p1_damage + 3
                        print ('Now player1 mp =', p1_mp)
                        print ('Player1 damage =', p1_damage)
                    else :
                        attackTurn = True
            elif player.character == 'Demon' :
                if p1_mp > 2 :
                    print ('Do you want to use 3 Mp for at + 2 and Hp + 1 ?')
                    print ('1.Yes')
                    print ('2.No')
                    useSkill = player.useSkill(p1_mp)
                    if useSkill == '1' :
                        p1_mp = p1_mp - 3
                        p1_damage = p1_damage + 2
                        player.hp = player.hp + 1
                        print ('Now player1 Mp =', p1_mp)
                        print ('Player1 damage =', p1_damage)
                    else :
                        p1_mp, p1_damage, attackTurn = normalAttack(p1_mp, p1_damage, attackTurn, player)
                        print ('Now player1 Mp =', p1_mp)
                        print ('Player1 damage =', p1_damage)
                else :
                        p1_mp, p1_damage, attackTurn = normalAttack(p1_mp, p1_damage, attackTurn, player)
                        print ('Now player1 Mp =', p1_mp)
                        print ('Player1 damage =', p1_damage)
            else :
                    p1_mp, p1_damage, attackTurn = normalAttack(p1_mp, p1_damage, attackTurn, player)
                    print ('Now player1 Mp =', p1_mp)
                    print ('Player1 damage =', p1_damage)

            if p1_mp < 2:
                attackTurn = True
     
    end = player.endTrun()
    print ('-------------------------------------')
    print ('## Player2 defense and attack turn ##')
    print ('- Player2 is a', player2.character)
    print ('- Player2 Mp =', p2_mp)
    print ('Player1 damage =', p1_damage)
    loop = False
    while (loop == False) :
        if player2.hand == [] :
            loop = True
            print ()
            print ('- No card to use')
            print ()
        else :
            checkCard = False
            while (checkCard == False) :
                if player2.hand == [] :
                    checkCard = True
                    loop = True
                else :
                    print ('Now player2 Mp =', p2_mp)
                    print ()
                    player2.showHand()
                    print ()
                    print ('You have', len(player2.hand), 'card')
                    print ('Input number to use item card & q to do not use card')
                    chooseCard = player2.chooseADCard(p2_mp, player2)
                    if chooseCard == 'q' or chooseCard == '' :
                        print ('- Do not use card')
                        checkCard = True
                        loop = True
                    else :
                        chooseCard = int(chooseCard)
                        if chooseCard > len(player2.hand) :
                                print ('You have', len(player2.hand), 'card')
                        else :
                            chooseCard = chooseCard - 1
                            p2_mp = p2_mp - player2.hand[chooseCard].mp
                            if p2_mp < 0 :
                                p2_mp = p2_mp + player2.hand[chooseCard].mp
                                print ('# Can not use the card #')
                            else :
                                print ('- Use the card')
                                print ()
                                print ('Now p2_mp is', p2_mp)
                                detail = player2.hand[chooseCard].detail.split('+')
                                if detail[0] == 'At' :
                                    p2_damage = p2_damage + int(detail[1])
                                    print ('Now damage is', p2_damage)
                                    player2.hand.remove(player2.hand[chooseCard])
                                elif detail[0] == 'Hp' :
                                    player2.hp = player2.hp + int(detail[1])
                                    player2.hand.remove(player2.hand[chooseCard])
                                    print ('Now player1 hp =', player2.hp )
                                elif detail[0] == 'Mp' :
                                    p2_mp = p2_mp + int(detail[1])
                                    player2.hand.remove(player2.hand[chooseCard])
                                    print ('Now player2 Mp =', p1_mp)
                                elif detail[0] == 'Shield' :
                                    p1_damage = p1_damage - int(detail[1])
                                    player2.hand.remove(player2.hand[chooseCard])
                                    if p1_damage < 0 :
                                        p1_damage = 0
                                    print ('Now player1 damage =', p1_damage)

    if p2_mp >= 1 and player2.character == 'Robot' :
        print ('- Player2 is a', player2.character)
        print ('Now player2 mp =', p2_mp)
        print ('Do you want to use 1 Mp for shield + 2 ? ')
        print ('1.Yes')
        print ('2.No')
        useSkill = player2.useSkill(p2_mp)
        if useSkill == '1' :
            p2_mp = p2_mp - 1
            p1_damage = p1_damage - 2
            if p1_damage < 0 :
                p1_damage = 0 
            print ('Now player2 Mp =', p2_mp)
            print ('Now player1 damage =', p1_damage)
            if p2_mp > 1 :
                normalLoop = False
                while ( normalLoop == False) :
                    p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                    print ('Now player2 mp =', p2_mp)
                    print ('Player2 damage =', p2_damage)
                    if p2_mp < 2 :
                        normalLoop = True
        else :
            if p2_mp > 1 :
                normalLoop = False
                while ( normalLoop == False) :
                    p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                    print ('Now player2 mp =', p2_mp)
                    print ('Player2 damage =', p2_damage)
                    if p2_mp < 2 :
                        normalLoop = True
    elif p2_mp > 1 :
        if player2.character == 'Priest' :
            print ('Do you want to use 2 Mp for Hp + 2 ?')
            print ('1.Yes')
            print ('2.No')
            useSkill = player2.useSkill(p2_mp)
            if useSkill == '1' :
                p2_mp = p2_mp - 2
                player2.hp = player2.hp + 2
                print ('Now player2 Mp =', p2_mp)
                print ('Player2 Hp + 2 =', player2.hp)
                if p2_mp > 1 :
                    normalLoop = False
                    while ( normalLoop == False) :
                        p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                        print ('Now player2 mp =', p2_mp)
                        print ('Player2 damage =', p2_damage)
                        if p2_mp < 2 :
                            normalLoop = True
            else:
                if p2_mp > 1 :
                    normalLoop = False
                    while ( normalLoop == False) :
                        p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                        print ('Now player2 mp =', p2_mp)
                        print ('Player2 damage =', p2_damage)
                        if p2_mp < 2 :
                            normalLoop = True 
        elif player2.character == 'Swordman' :
            normalLoop = False
            while (normalLoop == False) :
                if p2_mp > 2 :
                    print ('Do you want to use 3 Mp for at + 4 ?')
                    print ('1.Yes')
                    print ('2.No')
                    useSkill = player2.useSkill(p2_mp)
                    if useSkill == '1' :
                        p2_mp = p2_mp - 3
                        p2_damage = p2_damage + 4
                        print ('Now player2 Mp =', p2_mp)
                        print ('Player2 damage =', p2_damage)
                    else :
                        print ('Do you want to use 2 Mp for at + 3 ?')
                        print ('1.Yes')
                        print ('2.No')
                        useSkill = player2.useSkill(p2_mp)
                        if useSkill == '1' :
                            p2_mp = p2_mp - 2
                            p2_damage = p2_damage + 3
                            print ('Now player2 Mp =', p2_mp)
                            print ('Player2 damage =', p2_damage)
                        else :
                            normalLoop = True
                else :
                    print ('Do you want to use 2 Mp for at + 3 ?')
                    print ('1.Yes')
                    print ('2.No')
                    useSkill = player2.useSkill(p2_mp)
                    if useSkill == '1' :
                        p2_mp = p2_mp - 2
                        p2_damage = p2_damage + 3
                        print ('Now player2 Mp =', p2_mp)
                        print ('Player2 damage =', p2_damage)
                    else :
                        normalLoop = True
                if p2_mp < 2 :
                    normalLoop = True
        elif player2.character == 'Demon' :
            if p2_mp >= 3 :
                print ('Do you want to use 3 Mp for at + 2 and Hp + 1 ?')
                print ('1.Yes')
                print ('2.No')
                useSkill = player2.useSkill(p2_mp)
                if useSkill == '1' :
                    p2_mp = p2_mp - 3
                    p2_damage = p2_damage + 2
                    player2.hp = player2.hp + 1
                    print ('Now player2 Mp =', p2_mp)
                    print ('Player2 damage =', p2_damage)
                    print ('Player2 Hp =', player2.hp)
                    if p2_mp > 1 :
                        normalLoop = False
                        while ( normalLoop == False) :
                            p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                            print ('Now player2 mp =', p2_mp)
                            print ('Player2 damage =', p2_damage)
                            if p2_mp < 2 :
                                normalLoop = True
                else :
                    if p2_mp > 1 :
                        normalLoop = False
                        while ( normalLoop == False) :
                            p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                            print ('Now player2 mp =', p2_mp)
                            print ('Player2 damage =', p2_damage)
                            if p2_mp < 2 :
                                normalLoop = True
            else :
                normalLoop = False
                while ( normalLoop == False) :
                    p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                    print ('Now player2 mp =', p2_mp)
                    print ('Player2 damage =', p2_damage)
                    if p2_mp < 2 :
                        normalLoop = True
        else :  
            normalLoop = False
            while ( normalLoop == False) :
                p2_mp, p2_damage, normalLoop = normalAttack(p2_mp, p2_damage, normalLoop, player2)
                print ('Now player2 mp =', p2_mp)
                print ('Player2 damage =', p2_damage)
                if p2_mp < 2 :
                    normalLoop = True

    
    end = player2.endTrun()
    print ('-------------------------------------')
    print ()
    print ('## Player1 defense turn ##')
    print ('Now player1 Mp =', p1_mp)
    print ('Player2 damage =', p2_damage)
    loop = False
    while (loop == False) :
        if player.hand == [] :
            loop = True
            print ()
            print ('- No card to use')
            print ()
        else :
            checkCard = False
            while (checkCard == False) :
                if player.hand == [] :
                    checkCard = True
                    loop = True
                    print ('- Not use card')
                    print ()
                else :
                    print ()
                    player.showHand()
                    print ()
                    print ('You have', len(player.hand), 'card')
                    print ('Input number to use item card & q to do not use card')
                    chooseCard = player.chooseDefenseCard(p1_mp,  player2)
                    if chooseCard == 'q' or chooseCard == '':
                        print ('- No item card to use')
                        checkCard = True
                        loop = True
                    else :
                        chooseCard = int(chooseCard)
                        if chooseCard > len(player.hand) :
                            print ('You have', len(player.hand), 'card')
                        else :
                            chooseCard = chooseCard - 1
                            p1_mp = p1_mp - player.hand[chooseCard].mp
                            if p1_mp < 0 :
                                p1_mp = p1_mp + player.hand[chooseCard].mp
                                print ('# Can not use the card #')
                            else :
                                print ('Use the card')
                                print ('Now p1_mp is', p1_mp)
                                detail = player.hand[chooseCard].detail.split('+')
                                if detail[0] == 'At' :
                                    print ('Can not use')
                                elif detail[0] == 'Hp' :
                                    player.hp = player.hp + int(detail[1])
                                    player.hand.remove(player.hand[chooseCard])
                                    print ('Now player1 hp =', player.hp )
                                elif detail[0] == 'Mp' :
                                    p1_mp = p1_mp + int(detail[1])
                                    player.hand.remove(player.hand[chooseCard])
                                    print ('Now player1 Mp =', p1_mp)
                                elif detail[0] == 'Shield' :
                                    p2_damage = p2_damage - int(detail[1])
                                    player.hand.remove(player.hand[chooseCard])
                                    if p2_damage < 0 :
                                        p2_damage = 0
                                    print ('Player2 damage =', p2_damage)
                
        
    if p1_mp >= 1 and player.character == 'Robot' :
        print ('- Player1 is a', player.character)
        print ('Now player1 mp =', p1_mp)
        print ('Do you want to use 1 Mp for shield + 2 ? ')
        print ('1.Yes')
        print ('2.No')
        useSkill = player.useSkill(p1_mp)
        if useSkill == '1' :
            p1_mp = p1_mp - 1
            p2_damage = p2_damage - 2
            if p2_damage < 0 :
                p2_damage = 0 
            print ('Now player1 Mp =', p1_mp)
            print ('Now player2 damage =', p2_damage)
    elif p1_mp >= 1 and player.character == 'Priest'  :
        priest = False
        while (priest == False) :
            if player.character == 'Priest' :
                print ('Do you want to use 2 Mp for Hp + 2 ?')
                print ('1.Yes')
                print ('2.No')
                useSkill = player.useSkill(p1_mp)
                if useSkill == '1' :
                    p1_mp = p1_mp - 2
                    player.hp = player.hp + 2
                    print ('Now player1 Hp =', player.hp)
                    print ('Now player1 Mp =', p1_mp)
                else:
                    priest = True
            if p1_mp < 2 :
                priest = True

    end = player.endTrun()
    player.hp = player.hp - p2_damage
    player2.hp = player2.hp - p1_damage

    if turn == False :
        print ('====================================================')
        print ('Player is attacked', p2_damage, 'Damage')
        print ('Bot is attacked', p1_damage, 'Damage')
        print ('==================== End Battle ====================')
    else :
        print ('====================================================')
        print ('Bot is attacked', p2_damage, 'Damage')
        print ('Player is attacked', p1_damage, 'Damage')
        print ('==================== End Battle ====================')


