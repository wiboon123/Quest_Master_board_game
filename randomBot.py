import ItemCard
import random
import chooseCharacter

class Bot :
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
          number = random.randint(1, len(self.hand))
          if number > 0 and number < len(self.hand):
            number = int(number)
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

    def chooseNormalAttack(self, bot_mp) :
      rand = random.randint(1, 2)
      return rand

    def chooseWalk (self) :
      rand = random.randint(1, 2)
      return rand
      
    def checkItemcard (self) :
      if len(self.hand) > 5 :
        self.disCard()

    def chooseBattle(self, enemy) :
      number = random.randint(1, 2)
      return number
    
    def chooseDice (self, red, blue, p2) :
      number = random.randint(1, 2)
      return number
    
    def detailEvent(self, event) :
      number = random.randint(1, 2)
      return number

    def showCard(self) :
      return ''

    def chooseWarp(self, player2) :
        number = random.randint(1, 6)
        return number

    def endTrun(self) :
        end = None
        return end
    
    def enter(self) :
      enter = None
      return enter

    def chooseAttackCard (self, bot_mp, player2) :
      if self.hand == [] :
        return ''
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'At card' and self.hand[i].mp <= bot_mp :
            card.append(i)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i)
        card.append('')
        rand = random.randint(0, len(card) - 1 )
        if rand == 0 :
          return card[0]
        elif rand == 1 :
          return card[1]
        elif rand == 2 :
          return card[2]
        elif rand == 3 :
          return card[3]
        elif rand == 4 :
          return card[4]
        elif rand == 5:
          return card[5]

    def chooseADCard (self, bot_mp, player2) :
      if self.hand == [] :
        return ''
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'At card' and self.hand[i].mp <= bot_mp :
            card.append(i)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i)
          elif self.hand[i].typeCard == 'Df card' and self.hand[i].mp <= bot_mp :
            card.append(i)
        card.append('')
        rand = random.randint(0, len(card) - 1 )
        if rand == 0 :
          return card[0]
        elif rand == 1 :
          return card[1]
        elif rand == 2 :
          return card[2]
        elif rand == 3 :
          return card[3]
        elif rand == 4 :
          return card[4]
        elif rand == 5:
          return card[5]
         
    def chooseDefenseCard (self, bot_mp, player2) :
      if self.hand == [] :
        return ''
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'Df card' and self.hand[i].mp <= bot_mp :
            card.append(i)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i)
        card.append('')
        rand = random.randint(0, len(card) - 1 )
        if rand == 0 :
          return card[0]
        elif rand == 1 :
          return card[1]
        elif rand == 2 :
          return card[2]
        elif rand == 3 :
          return card[3]
        elif rand == 4 :
          return card[4]
        elif rand == 5:
          return card[5]


    def useSkill (self, bot_mp) :
      number = random.randint(1, 2)
      number = str(number)
      return number
    
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
    