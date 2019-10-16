import eventCard
import Player
import ItemCard
import random
import battle
import randomBot
import RuleBot


def checkBoard(check, player, eventCards, deck, turn, player1, player2) :
  event = eventCards
  enemy = player2
  if check[1] == ['I'] :
    print ('get 1 item card') 
    player.draw(deck)
  elif check[1] == ['E'] :
    item = 0
    event, item = eventCard.eventCard(player, event, player2, deck, turn)
    if item == 1 :
      player.draw(deck)
    elif item == 2 :
      player.draw(deck)
      player.draw(deck)
  elif check[1] == ['W'] :
    print ('Warp portal')
    print ('1. go to warp portal [P12]')
    print ('2. go to warp portal [J2]')
    print ('3. go to warp portal [A6]')
    print ('4. go to warp portal [G9]')
    print ('5. go to warp portal [H3]')
    print ('6. Do not warp')
    number = player.chooseWarp(player2)
    if number == 1 :
      print ('You are going to the warp portal [P12]')
      player.position = 17
    elif number == 2 :
      print ('You are going to the warp portal [J2]')
      player.position = 39
    elif number == 3 :
      print ('You are going to the warp portal [A6]')
      player.position = 56
    elif number == 4 :
      print ('You are going to the warp portal [G9]')
      player.position = 65
    elif number == 5 :
      print ('You are going to the warp portal [H3]')
      player.position = 91
    elif number == 6 :
      print ('Do not warp')
  elif check[1] == ['B'] :
    print ('Do you want to battle ?')
    print ('1.Battle')
    print ('2.No battle')
    choose = player.chooseBattle(enemy)
    if choose == 1 :
      print ('## Battle ##')
      battle.battle(player, player2, turn)
    else :
      print ('No Battle')
  elif check[1] == ['P'] :
    priestCastle(player)
  elif check[1] == ['M'] :
    magicSchool(player, enemy, deck)
  elif check[1] == ['D'] :
    demonCastle(player, enemy, deck)
  elif check[1] == ['F'] :
    factoryCastle(player, deck)
  elif check[1] == ['S'] :
    swordCastle(player, deck)
  elif check[1] == ['4'] :
    player.hp = player.hp - 4
    print ('Player HP - 4 =', player.hp)
  elif check[1] == ['3'] :
    player.hp = player.hp - 3
    print ('Player HP - 3 =', player.hp)
  elif check[1] == ['2'] :
    player.hp = player.hp  - 2
    print ('Player HP - 2 =', player.hp)
  elif check[1] == ['1'] :
    player.hp = player.hp - 1
    print ('Player HP - 1 =', player.hp)
  return event

def demonCastle (player, enemy, deck) :
  print ('## You are in the haunted house ##')
  player.addCastle('D')
  if player.character == 'Demon' :
    print ('Hp + 6 and enemy hp - 2')
    player.hp = player.hp + 6
    print ('Your Hp is', player.hp)
    enemy.hp = enemy.hp - 2
    print ('Enemy Hp is', enemy.hp)
  else :
    blueDice = [1,2,3,4,"Item","Event"]
    blue = random.choice(blueDice)
    print ("The blue dice is ", blue)
    if blue == 'Event' :
      player.hp = player.hp - 2
      print ('Your Hp - 2 =', player.hp)
    elif blue == 'Item' :
      print ('get 1 item card')
      player.draw(deck)
    else :
      print ('Enemy Hp decrease to the number of pitches is')
      enemy.hp = enemy.hp - blue
      print ('Enemy Hp - ',blue, ' = ', enemy.hp)
  
def swordCastle (player, deck) :
  print ('## You are in the Castle ##')
  player.addCastle('S')
  if player.character == 'Swordman' :
    print ('get 2 item card')
    player.draw(deck)
    player.draw(deck)
  else :
    print ('get 1 item card')
    player.draw(deck)

def priestCastle (player) :
  print ('## You are in the chuch ##')
  player.addCastle('P')
  if player.character == 'Priest' :
    print ('Hp + 5')
    player.hp = player.hp + 5
  else :
    redDice = [1,2,3,4,"Battle","Battle"]
    red = random.choice(redDice)
    print ("The red dice is ", red)
    if red == 'Battle' :
      print ('Hp + 1')
      player.hp = player.hp + 1
    else :
      print ('Hp incresae to the number of pitches is', red)
      player.hp = player.hp + red
    print ('Your Hp is', player.hp)

def factoryCastle (player, deck) :
  print ('## You are in the Factory ##')
  player.addCastle('F')
  if player.character == 'Robot' :
    print ('Hp + 3 and get 1 item card')
    player.draw(deck)
    player.hp = player.hp + 3
    print ('Your Hp is', player.hp)
  else :
    print ('get 1 item card')
    player.draw(deck)

def magicSchool (player, enemy, deck) :
  print ('## You are in the magic school ##')
  player.addCastle('M')
  if player.character == 'Magician' :
    print ('Enemy Hp - 2')
    enemy.hp = enemy.hp - 2
    print ('Enemy Hp is', enemy.hp)
  else :
    redDice = [1,2,3,4,"Battle","Battle"]
    red = random.choice(redDice)
    print ("The red dice is ", red)
    if red == 'Battle' :
      print ('get 1 item card')
      player.draw(deck)
    else :
      print ('Enemy Hp decrease to the number of pitches is', red)
      enemy.hp = enemy.hp - red
      print ('Enemy Hp is', enemy.hp)