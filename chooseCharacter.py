import random

def chooseOne() :
      choose = False
      while (choose == False) :
          print ('Please choose Number 1 - 5')
          number = input()
          if number == '1' or number == '2' or number == '3' or  number == '4' or number == '5'  :
              number = int(number)
              choose = True
              return number

def p1_character() :
    heros = ['Priest', "Magician", "Robot", "Swordman", "Demon"]
    for i in range(0,5):
        print((i+1),'.',heros[i])
    
    chooseCharacter = chooseOne()
    if chooseCharacter == 1 :
        character = "Priest"
        hp = 26
        position = 14
        status = 0
        print("You are Priest HP 26")
    elif chooseCharacter == 2 :
        character = "Magician"
        hp = 24
        position = 50
        status = 0
        print("You are Magician HP 24")
    elif chooseCharacter == 3 :
        character = "Robot"
        hp = 25
        position = 83
        status = 0
        print("You are Robot HP 25")
    elif chooseCharacter == 4 :
        character = "Swordman"
        hp = 23
        position = 2
        status = 0
        print("You are Swordman HP 25")
    else :
        character = "Demon"
        hp = 23
        position = 31
        status = 0
        print("You are Demon HP 23")
    return character, hp, position, status

def p2_character(player2) :
    if player2 == '2Player' :
        character, hp, position, status = p1_character()
    else :
        heros = ['Priest', "Magician", "Robot", "Swordman", "Demon"]
        character = random.choice(heros)
        if character == 'Priest' :
            hp = 26
            position = 14
            status = 0
            print ('Player2 is a Priest')
        elif character == 'Magician' :
            hp = 24
            position = 50
            status = 0
            print ('Player2 is a Magician', )
        elif character == 'Robot' :
            hp = 25
            position = 83
            status = 0
            print ('Player2 is a Robot', )
        elif character == 'Swordman' :
            hp = 23
            position = 2
            status = 0
            print ('Player2 is a Swordman', )
        elif character == 'Demon' :
            hp = 23
            position = 31
            status = 0
            print ('Player2 is a Demon', )
    return character, hp, position, status