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
      if self.hand == [] :
        return 1
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i)
          elif self.hand[i].typeCard == 'Df card' and self.hand[i].mp <= bot_mp :
            card.append(i)
        
        if len(card) > 0 :
          rand = random.randint(1, 2)
          if rand == 1 :
            return 1
          else :
            return 2
        else :
          return 1

    def chooseWalk (self) :
      for i in range(len(self.castle)) :
        if self.castle[i] == 'F' :
          return 1
      rand = random.randint(1, 2)
      return rand


    def checkItemcard (self) :
      if len(self.hand) > 5 :
        self.disCard()

    def chooseBattle(self, enemy) :
        if enemy.hp < 15 :
          if len(self.hand) > 2 :
            return 1
          else :
            rand = random.randint(1, 2)
            if rand == 1 :
              return 1
            else :
              return 2
        elif len(self.hand) > 2 :
          rand = random.randint(1, 2)
          if rand == 1 :
            return 1
          else :
            return 2
        else :
          return 2
      
    def chooseDice (self, red, blue, p2) :
      if red == 1 or red == 2 or red == 3 or red == 4 :
        check = red + self.position
        if check > 14 and check <= 17 or check > 50 and check <= 53 or check > 83 and check <= 86 or check > 31 and check <= 34 or check > 2  and check <= 5:
          return  2
        elif blue == 'Item' :
          if len(self.hand) < 4 :
            return 2
          else :
            rand = random.randint(1,2)
            return rand
        else :
          rand = random.randint (1, 2)
          return rand
      elif blue == 1 or blue == 2 or blue == 3 or blue == 4 :
        check = blue + self.position
        if check > 14 and check <= 17 or check > 50 and check <= 53 or check > 83 and check <= 86 or check > 31 and check <= 34 or check > 2  and check <= 5:
          return 1
        elif p2.hp <= 15 and self.hp > p2.hp :
          if len(self.hand) >= 2 :
            rand = random.randint(1, 4)
            if rand < 4 :
              return 1
            else :
              return 2
          else :
              rand = random.randint(1, 2)
              return rand
        elif red == 'Battle' and blue == 'Item' or blue == 'Event' :
          if blue == 'Item' :
            if self.hand <= 3 :
              return 2
            else :
              rand = random.randint (1, 2)
              return rand
          elif self.hp < 15 :
            if p2.hp < self.hp :
              if self.hand >= 2 :
                return 1
              else :
                rand = random.randint (1, 2)
                return rand 
            else :
              return 2
          else :
            if len(self.hand) >= 3 :
              rand = random.randint(1, 4)
              if rand < 4 :
                return 1
              else :
                return 2
            else :
              return 2
              
    def showCard(self) :
      return ''

    def detailEvent(self, event) :
      if event == 14 :
        if self.hp <= 15 :
          return 2
        else :
          return 1 
      elif event == 19 :
        if self.hp <= 18 :
          return 1
        else :
          return 2

    def chooseWarp(self, player2) :
        if self.hp < 13 :
          return 4
        elif player2.hp < 13 :
          rand = random.randint (1, 4)
          if rand == 1 :
            return 1
          elif rand == 2 :
            return 2 
          elif rand == 3 :
            return 5 
          else :
            return 6
        elif self.castle == [] :
          rand = random.randint (1, 4)
          if rand == 1 :
            return 2
          elif rand == 2 :
            return 4 
          elif rand == 3 :
            return 5 
          else :
            return 6
        else :
          if self.hp >= 30 :
            return 4
          elif player2.hp >= 30 :
            rand = random.randint (1, 4)
            if rand == 1 :
              return 1
            elif rand == 2 :
              return 2 
            elif rand == 3 :
              return 5 
            else :
              return 6
          else :
            rand = random.randint (1, 4)
            if rand == 1 :
              return 2
            elif rand == 2 :
              return 4 
            elif rand == 3 :
              return 5 
            else :
              return 6

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
            card.append(i + 1)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)
        
        number = self.useCard(card, bot_mp)
        return str(number)


    def chooseADCard (self, bot_mp, player2) :
      if self.hand == [] :
        return ''
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'At card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)
          elif self.hand[i].typeCard == 'Df card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)
        
        number = self.useCard(card, bot_mp)
        return str(number)


    def chooseDefenseCard (self, bot_mp, player2) :
      if self.hand == [] :
        return ''
      else :
        card = []
        for i in range(len(self.hand) - 1) :
          if self.hand[i].typeCard == 'Df card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)
          elif self.hand[i].typeCard == 'AD card' and self.hand[i].mp <= bot_mp :
            card.append(i + 1)

        number = self.useCard(card, bot_mp)
        return str(number)

    def useCard(self, card, bot_mp ) :
      for i in range(len(card)) :
        if self.hand[card[i]].mp == 0 :
          return card[i]
        elif bot_mp >= 1 :
          if self.character == 'Robot' :
            rand = random.randint(1, 2)
            if rand == 1 :
              return card[i]
            else :
              return ''
          elif self.character == 'Swordman' :
            rand = random.randint(1, 3)
            if rand == 3 :
              return card[i]
            else :
              return ''
          elif self.character == 'Priest' :
            if self.hp < 15 or self.hp > 30 :
              rand = random.randint(1, 3)
              if rand == 3 :
                return card[i]
              else :
                return ''
            else :
              rand = random.randint(1, 2)
              if rand == 1 :
                return card[i]
              else :
                return ''
          else :
            rand = random.randint(1, 2)
            if rand == 1 :
              return card[i]
            else :
              return ''
        else :
          return ''


    def useSkill (self, bot_mp) :
      if self.character == 'Swordman' :
        if bot_mp >= 3 :
          rand = random.randint(1, 6)
          if rand == 1 :
            return 1
          else :
            return 2
        elif bot_mp == 2 :
          return '1'
      elif self.character == 'Priest' :
        if bot_mp >= 2 :
          return '1'
      elif self.character == 'Demon':
        if bot_mp >= 3 :
          return '1'
      elif self.character == 'Robot' :
        if bot_mp == 1 :
          return '1'
        elif bot_mp == 2 :
          if self.character < 15 :
            return '1'
          else :
            return '2'
      else :
        return '2'
      
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
    