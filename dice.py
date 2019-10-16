import random
import Player
import randomBot
import RuleBot

def rollTheDice(turn, player, cards, p2) :
  print("# Roll the dice #")
  redDice = [1,2,3,4,"Battle","Battle"]
  blueDice = [1,2,3,4,"Event","Item"]
  red = random.choice(redDice)
  blue = random.choice(blueDice)
  print ("-------------------------------------------")
  print ("The red dice is ", red)
  print ("The blue dice is ", blue)
  print ("-------------------------------------------")
  if red == 1 or red == 2 or red == 3 or red == 4 :
    if blue == 1 or blue == 2 or blue == 3 or blue == 4 :
      walk = red + blue
      print("Walk = ", walk)
      return walk
    else :
      print("Choose one dice")
      print ("1.", red)
      print ("2.", blue)
      chooseDice = player.chooseDice(red, blue, p2)
      if chooseDice == 1 :
        print ("You choose red dice is", red)
        walk = red
        print ('Walk = ', walk)
        return walk
      else :
        print ("You choose blue dice is", blue)
        if blue == 'Event' :
          event = 'Event'
          return event
        else :
          item = 'Item'
          return item
  else : 
    if blue == 1 or blue == 2 or blue == 3 or blue == 4 :
      print("Choose one dice") 
      print("1.", red)
      print("2.", blue)
      chooseDice = player.chooseDice(red, blue, p2)
      if chooseDice == 1 :
        print ("You choose red dice is", red)
        battle = 'Battle'
        return battle
      else :
        print ("You choose blue dice is", blue)
        walk = blue
        print ('Walk = ', walk)
        return walk
    else :
      print("Choose one dice") 
      print("1.", red)
      print("2.", blue)
      chooseDice = player.chooseDice(red, blue, p2)
      if chooseDice == 1 :
        print ("You choose red dice is", red)
        battle = 'Battle'
        return battle
      else :
        print ("You choose blue dice is", blue)
        if blue == 'Item' :
          item = 'Item'
          return item
        else :
          event = 'Event'
          return event