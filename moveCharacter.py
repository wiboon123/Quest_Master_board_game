import Player
import randomBot

def move(player, move) :
  playerPosition = player.position
  if playerPosition > 46 and playerPosition <= 54 :
    playerPosition = playerPosition + move
    if playerPosition >= 55 :
      print ('choose the way')
      print ('1. go to castle')
      print ('2. go to factory')
      chooseOne = player.chooseWalk()
      if chooseOne == 2 :
        if playerPosition == 55 :
          playerPosition = 76
        elif playerPosition == 56 :
          playerPosition = 77
        elif playerPosition == 57 :
          playerPosition = 78 
        elif playerPosition == 58 :
          playerPosition = 79
        elif playerPosition == 59 :
          playerPosition = 80
        elif playerPosition == 60 :
          playerPosition = 81 
        elif playerPosition == 61 :
          playerPosition = 82
        else :
          playerPosition = 83 
  elif playerPosition < 76 :
    playerPosition = playerPosition + move
    if playerPosition == 76 :
      playerPosition = 0
    elif playerPosition == 77 :
      playerPosition = 1 
    elif playerPosition == 78 :
      playerPosition = 2
    elif playerPosition == 79 :
      playerPosition = 3
    elif playerPosition == 80 :
      playerPosition = 4
    elif playerPosition == 81 :
      playerPosition = 5
    elif playerPosition == 82 :
      playerPosition = 6 
    elif playerPosition == 83 :
      playerPosition = 7
  else :
    playerPosition = playerPosition + move
    if playerPosition == 96 :
      playerPosition = 45
    elif playerPosition == 97 :
      playerPosition = 46
    elif playerPosition == 98 :
      playerPosition = 47
    elif playerPosition == 99 :
      playerPosition = 48
    elif playerPosition == 100 :
      playerPosition = 49
    elif playerPosition == 101 :
      playerPosition = 50
    elif playerPosition == 102 :
      playerPosition = 51
    elif playerPosition == 103 :
      playerPosition = 52
  return playerPosition
