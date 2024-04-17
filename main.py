import math
import random

#I import my classes
import classes

def greet():
        print("        \\    \\    //      \\      ")
        print("       / \\   )\\__//(     / \\     ")
        print("      /   \\ (_\\  //_)   /   \\    ")
        print(" ____/____\\__\\@  @//___/_____\\__ ")
        print("|             |\\..//|             |")
        print("|              \\VV/               |")
        print("|      Welcome to Ju-Racist Park   |")
        print("|__________________________________|")
        print(" |    /\\ /       \\   \ / \\ /\\  |")
        print(" |   /   V         ))   v    V  \\ |")
        print(" |  /     `       //        '    \\|")
        print(" `//              V                '")


start = input("Enter 'start' to start the game: ")

if start == 'start':
    greet()
    
your_character =  "" 

character_choice = input("Chose your charcacter. 1: Paladin.   2: Witch.     3:Barbarian.")
print("______________________________________")
if character_choice == "1":
    your_character = classes.paladin_hero
    charName = input("What is your name, Paladin?: ")
    classes.paladin_hero.name = charName
    print("Greetings Paladin", your_character.name)
elif character_choice == "2":
    your_character = classes.witch_hero
    charName = input("What is your name, Witch?: ")
    classes.witch_hero.name = charName
    print("Greetings Witch", your_character.name)
    
else:
    your_character = classes.barbarian_hero   
    charName = input("What is your name, Barbarian?: ")
    classes.barbarian_hero.name = charName
    print("Greetings Barbarian", your_character.name)
    


print("""                       
        \ \   / /                             | |                   | |                          | |              | |        | |                     
         \ \_/ /___   _   _  _ __    __ _   __| |__   __ ___  _ __  | |_  _   _  _ __  ___   ___ | |_  __ _  _ __ | |_  ___  | |__    ___  _ __  ___ 
          \   // _ \ | | | || '__|  / _` | / _` |\ \ / // _ \| '_ \ | __|| | | || '__|/ _ \ / __|| __|/ _` || '__|| __|/ __| | '_ \  / _ \| '__|/ _ \
           | || (_) || |_| || |    | (_| || (_| | \ V /|  __/| | | || |_ | |_| || |  |  __/ \__ \| |_| (_| || |   | |_ \__ \ | | | ||  __/| |  |  __/
           |_| \___/  \__,_||_|     \__,_| \__,_|  \_/  \___||_| |_| \__| \__,_||_|   \___| |___/ \__|\__,_||_|    \__||___/ |_| |_| \___||_|   \___|
                                                                                                                                                        """)
print(f"You spawned in a {your_character.place} . Defeat {classes.Steven.name} in the forest in order to win.")

inventory = classes.Inventory()
skeleton = classes.Mob("skeleton", 40, 40, 20, 10, 1)

distance = 0
# new_distance = distance + 1


while your_character.hp > 0:
    if your_character.place == "village":
        initialChoice = input("what to do ?: 1.Explore the forest  |  2.Store   |   3.Sleep   ")
        if initialChoice == "1":
                your_character.place = "forest"
                print(f"You venture into the ", your_character.place)
                print("You have travelled: ", distance + 1, 'km deep into the forest')
        elif initialChoice =="2":
                buyOption= input("You go to the marketplace.. What do you want to buy ? 1.Potion🧪  |   2.Poison flask ☣️") 
                if buyOption == "1":
                    if your_character.gold < 15:
                        print("You do not have enough gold.. Sell some items first.")
                    else:     
                        inventory.add("1 Potion 🧪")
                        your_character.gold -= 15
                        print("Your items: ", inventory.content)
                        print("Your goldcoins 📀:", your_character.gold)
                elif buyOption == "2":
                    if your_character.gold < 20:
                        print("You do not have enough gold.. Sell some items first.")
                    else:     
                        your_character.gold -= 20
                        inventory.add("1 Poison flask ☣️")
                        print("Your items: ", inventory.content)
                        print("Your goldcoins 📀:", your_character.gold)

        else:
                sleepRequest = input("You go to the Inn and ask for a bed. It will cost you 10 coins for the night. Do you accept?: 'y/n':  ")

                if sleepRequest == "y":
                    your_character.gold -= 10 
                    your_character.hp = your_character.maxHp
                    if your_character.gold < 10:
                        print("You do no have enough gold! Sell some items first.")
                    else:   
                        print("Your recovered your health..  goldcoins 📀: ", your_character.gold) 
                else:
                    print("You declined the offer.")      
                    
    else:
        secondary_choice = input("What to do?   1.Explore the forest   |   2.Inventory:     |    3.Return to village")
        if secondary_choice == "1":
            print(f"{your_character.name} is venturing deep into the forest...")
            distance +=1
            print("You have travelled: ", distance + 1, 'km deep into the forest')

            random_num = random.random()

            #This will determine what happens every time we choose to explore the forest
            possibilities = ["combat", "randomItems", "nothing"]
            randomAction = possibilities[math.floor(random_num*len(possibilities))]
            # _________________________________

            #This will determine what items you find
            itemPossibilites = ["Potion", "goldcoins 📀", "50xp points"]
            randomItem = itemPossibilites[math.floor(random_num*len(possibilities))]
            # _________________________________

            current_action = randomAction
            if current_action == "combat":
                print(f"{your_character.name} got ganked by a  {classes.creep.name} ")
                while your_character.hp > 0 and skeleton.hp > 0:
                    print(f"{classes.creep.name} jumped on you!")
                    
                    skeleton.normal_attack(your_character)
                    print(f"{your_character.name}'HP: {your_character.hp}")
                    heroAttack = input(f"Press '1' to attack {classes.creep.name}: ")
                    if heroAttack == "1":
                        your_character.frozen_orb(skeleton)
                        print(f"{skeleton.name}'HP: {skeleton.hp}")  
                        if skeleton.hp <= 0:
                            your_character.lvl += 1
                            gainedGold = math.floor(random_num*30)
                            your_character.gold += gainedGold
                            print(f"{classes.creep.name} died..☠  {your_character.name} leveled up!")
                            print(f"{classes.creep.name} dropped {gainedGold} goldcoins 📀")
                            print(f"Your current level: {your_character.lvl}")
                            print(f"Your goldcoins stack : {your_character.gold} 📀")
                            


                    else:
                        print("Please enter '1' ")    
                skeleton.hp = skeleton.maxHp


                
            elif current_action == "nothing":
                print(f"{your_character.name} is venturing deep into the forest... this forest is too still...")
            else:
                print(f"{your_character.name} is venturing deep into the forest... {your_character.name} found an item!")
                itemsInput = input("Pick up item?  'y'/'n' : ")
                if itemsInput == "y":
                    inventory.add(randomItem)
                    print(f"{your_character.name}  picked up {randomItem}.  Your items:  {inventory.content}")
                else:
                    print(f"{your_character.name} opted not to pick up {randomItem}")   
            continue    
        elif secondary_choice == "3":
             your_character.place = "village"
             
        else:
            print(inventory.content)
           
