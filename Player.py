import ItemCard
import random
import chooseCharacter

class Player :
    def __init__ (self, character, hp, position, status) :
      self.character = character
      self.hp = hp
      self.position = position
      self.status = status
      self.hand = []
      self.castle = []
      

    def draw(self, deck) :
      self.hand.append(deck.drawCard())
      return self

    def showHand(self) :
      for card in self.hand :
        card.show()


    def disCard(self) :
        print () 
        self.showHand()
        print ()
        loop = False
        while (loop == False) :
          print ('Please choose number to discard on your hand')
          number = input()
          if number == '1' or number == '2' or number == '3' or  number == '4' or number == '5' or number == '6' or number == '7' :
            number = int(number)
            if number > 0 and number <= len(self.hand) :
              loop = True
        if number == 1 :
            self.hand.remove(self.hand[0])
        elif number == 2 :
            self.hand.remove(self.hand[1])
        elif number == 3 :
            self.hand.remove(self.hand[2])
        elif number == 4 :
            self.hand.remove(self.hand[3])
        elif number == 5 :
            self.hand.remove(self.hand[4])
        elif number == 6 :
          self.hand.remove(self.hand[5])
        elif number == 7 :
          self.hand.remove(self.hand[6])
        print ('Discard completed')

    def checkItemcard (self) :
      if len(self.hand) > 5 :
        self.disCard()


    def chooseBattle(self, enemy) :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number
          
    def chooseDice (self, red, blue, p2) :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number

    def showCard(self) :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number 

    def chooseWalk (self) :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number

    def chooseNormalAttack(self, bot_mp)  :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number

    def detailEvent(self, event) :
      choose = False
      while (choose == False) :
        print ('Please choose 1 or 2')
        number = input()
        if number == '1' or number == '2'  :
          number = int(number)
          choose = True
          return number
        elif number == '' :
          choose = True
          return number

    def chooseWarp(self, player2) :
      choose = False
      while (choose == False) :
          print ('Please choose 1 - 6')
          number = input()
          if number == '1' or number == '2' or number == '3' or  number == '4' or number == '5' or number == '6'  :
              number = int(number)
              choose = True
              return number

    def endTrun(self) :
      end = input('[---- Please enter for end turn ----]')
    
    def enter(self) :
      enter = input()

    def chooseAttackCard (self, mp, player2) :
      choose = input()
      return choose
    
    def chooseADCard (self, mp, player2) :
      choose = input()
      return choose

    def chooseDefenseCard (self, mp, player2) :
      choose = input()
      return choose


    def useSkill(self, mp) :
      choose = input()
      return choose

    def addCastle (self, castle) :
      notSame = 0
      same = 1
      if self.castle == [] :
        self.castle.append(castle)
      else :
        for i in range (len(self.castle)) :
          if self.castle[i] != castle :
            notSame = notSame + 1
          else :
            same = same - 1
        if same > 0 :
          if notSame > 0 :
            self.castle.append(castle)
      return self

