print(r'''
            _......._
        .-'.'.'.'.'.'.`-.
      .'.'.'.'.'.'.'.'.'.`.
     /.'.'               '.\
     |.'    _.--...--._     |
     \    `._.-.....-._.'   /
     |     _..- .-. -.._   |
  .-.'    `.   ((@))  .'   '.-.
 ( ^ \      `--.   .-'     / ^ )
  \  /         .   .       \  /
  /          .'     '.  .-    \
 ( _.\    \ (_`-._.-'_)    /._\)
  `-' \   ' .--.          / `-'
      |  / /|_| `-._.'\   |
      |   |       |_| |   /-.._
  _..-\   `.--.______.'  |
       \       .....     |
        `.  .'      `.  /
          \           .'
           `-..___..-`
''')

def gameStart():
  print("Welcome to Cyclops Escape!\n")
  firstQuestion()

def restart():
  restart_tf = input("Would you like to try again? (Y/N)\n")

  if restart_tf.lower() == 'y':
    gameStart()
  elif restart_tf.lower() == 'n':
    print("Goodbye.")
    exit()
  else:
    print("Command not recognized. Please enter 'Y' or 'N'.\n")

def playAgain():
  play_again = input("Would you like to play again? (Y/N)\n")

  if play_again.lower() == 'y':
    gameStart()
  elif play_again.lower() == 'n':
    print("Goodbye.")
    exit()
  else:
    print("Command not recognized. Please enter 'Y' or 'N'.\n")
    playAgain()

def firstQuestion():
  run_hide = input("You see a cyclops walking towards you. Would you like to 'run' or 'hide'?\n")

  if run_hide.lower() == 'run':
    print("The cyclops sees you run away, and gives chase.\n")
    secondQuestion()
  elif run_hide.lower() == 'hide':
    print("You chose to hide in a nearby tree line. The cyclops sees you and tears down the trees, killing you in the process. Game Over.\n")
    restart()
  else:
    print("Command not recognized. Please enter 'run' or 'hide'.\n")
    firstQuestion()

def secondQuestion():
  swim_boat = input("You run into a neaby lake, the cyclops is still chasing you. You see a speedboat nearby. To cross the lake, do you 'swim' or use the 'boat'?\n")

  if swim_boat.lower() == 'boat':
    print("You get in the boat and start it just in time. You quickly speed across the lake, land on shore and find yourself looking into a forest.\n")
    thirdQuestion()
  elif swim_boat.lower() == 'swim':
    print("You start swimming, but the water is shallow. The cyclops wades over and eats you. Game Over.\n")
    restart()
  else:
    print("Command not recognized. Please enter 'swim' or 'boat'.\n")
    secondQuestion()

def thirdQuestion():
  three_options = input("The forest has three visible paths. Do you choose the 'left', the 'middle', or the 'right'?\n")

  if three_options.lower() == 'left':
    print("You have come across the end of my game.\n")
    playAgain()
  elif three_options.lower() == 'middle':
    print("Congrats!. This is the end of my game.\n")
    playAgain()
  elif three_options.lower() == 'right':
    print ("This is another possible ending.\n")
    playAgain()
  else:
    print("Command not recognized. Please enter 'left', 'middle', or 'right'.\n")

gameStart()
