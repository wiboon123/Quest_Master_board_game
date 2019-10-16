import random

class Card :
  def __init__(self, typeCard, mp, detail):
        self.typeCard = typeCard
        self.mp = mp
        self.detail = detail

    
  def show(self) :
    print ("[{}] Mp {} [ Detail : {} ]".format(self.typeCard, self.mp, self.detail))


class Deck :
  def __init__(self):
    self.cards = []
    self.build()

  def build(self) :
     self.cards.append(Card('At card', 0 ,'At+1'))
     self.cards.append(Card('At card', 1 ,'At+2'))
     self.cards.append(Card('At card', 0 ,'At+1'))
     self.cards.append(Card('AD card', 0 ,'Hp+3'))
     self.cards.append(Card('AD card', 0 ,'Mp+2'))
     self.cards.append(Card('AD card', 0 ,'Mp+1'))
     self.cards.append(Card('Df card', 0 ,'Shield+2'))
     self.cards.append(Card('Df card', 0 ,'Shield+1'))
     self.cards.append(Card('Df card', 1 ,'Shield+3'))
     self.cards.append(Card('AD card', 2 ,'Hp+5'))
     self.cards.append(Card('Df card', 2 ,'Shield+4'))
     self.cards.append(Card('At card', 2 ,'At+3'))


  def show(self) :
    for c in self.cards :
      c.show()

  def shuffle(self) :
    for i in range(len(self.cards)) :
      r = random.randint(0,i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
  
  def drawCard(self) :
    if self.cards == [] :
      self.build()
    return self.cards.pop()

