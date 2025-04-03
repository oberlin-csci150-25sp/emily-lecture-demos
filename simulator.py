import spaceship
import random

def random_encounter(player):
  ''' randomly determine what happens to the player 	ship when it moves. each scenario could modify the 	player ship and/or print a message. '''
  
  event = random.choice([0, 1, 2])
  
  if event == 0:
    print("No event. Smooth sailing!")
  elif event == 1:
    pass
  elif event == 2:
    pass
  
  return

def main():
    # Activity: 24.1 Creating Player Ship
    player_name = input("Welcome to the spaceship simulator! Name your ship: ")
    # player_ship = ???

    # Activity: Choices in Games
    done = False 
    turn = 0
    while (not done):
        print()
        print()
        print("Turn " + str(turn) + ": What would you like to do?")
        print("1 - show current speed")
        print("2 - boost speed")
        print("3 - move forward")
        print("0 - quit")
        
        select = input("Choice: ")
        
        if select == "1":
            print("(1) TODO - show current speed")
        elif select == "2":
            print("(2) TODO - boost speed")
        elif select == "3":
            print("(3) TODO - random_encounter")
            # random_encounter(player_ship) # TODO
        elif select == "0":
            print("Safe travels!")
            done = True
        
        turn += 1

main()