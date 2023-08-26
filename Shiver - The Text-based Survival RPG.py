"""

Serena Rojo
CIT 1213
---------------------------------------------------------------------------
Shiver: The Text-Based Survival RPG:
Your character is created, then you enter the story of wilderness survival.
---------------------------------------------------------------------------
started on:
4/16/2020

finished on:
5/10/2020

"""

#### Text-art ####
#Mountain
def mountain_art():
    print("        _    .  ,   .           .                      ")
    print("    *  / \_ *  / \_      _  *        *   /\'__        *")
    print("      /    \  /    \,   ((        .    _/  /  \  *'.   ")
    print(" .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.    ")
    print("    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *")
    print("  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ ")
    print(" /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-  ")
    print("/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._   ")

#Camp
def survive_art():
    print("                        (                              ")
    print("                         )                             ")
    print("                        (  (                           ")
    print("                            )                          ")
    print("                      (    (  ,,                       ")
    print("                       ) /\  ((                        ")
    print("                     (  // | (`'                       ")
    print("                   _ -.;_/ \\--._                      ")
    print("                  (_;-// | \ \-'.\                     ")
    print("                  ( `.__ _  ___,')                     ")
    print("                   `'(_ )_)(_)_)'                      ")

#Death
def death_art():
    print("                _____    _____   _____                 ")
    print("               |  __ \  |_   _| |  __ \                ")
    print("               | |__) |   | |   | |__) |               ")
    print("               |  _  /    | |   |  ___/                ")
    print("               | | \ \ _ _| |_ _| |_                   ")
    print("               |_|  \_(_)_____(_)_(_)                  ")

#### imports and stuff ####
import sys
screen_width = 100

#### Title Screen ####
def title_screen():
    mountain_art()
    print("-------------------------------------------------------")
    print("     Welome to Shiver: The Text-Based Survival RPG!    ")
    print("        -type in the answer to make that choice-       ")
    print("-------------------------------------------------------")
    print("                         -Play-                        ")
    print("                         -Help-                        ")
    print("                         -Quit-                        ")
    title_screen_selections()
    
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        print("Wow, what a loser! Can't handle a little cold? I didn't want")
        print("to hang out with you anyways! Later~                        ")
        sys.exit()

#### Help Menu ####
def help_menu():
    print("-------------------------------------------------------")
    print("                       Help Menu                       ")
    print("-------------------------------------------------------")
    print("-type in the answer to make that choice.               ")
    print("")
    print("-if your hunger, thirst, or warmth meter fall to zero, ")
    print(" you lose health. You can also lose health from        ")
    print(" getting injured throughout the story. If your health  ")
    print(" reaches zero at any point, you die and lose the game. ")
    print("")
    print("-at any time, type 'quit' to exit.                     ")
    print("")
    print("-good luck!                                            ")
    title_screen()

#### Game ####
def start_game():
    #player stats: 1
    player_health = 100
    player_hunger = 100
    player_thirst = 100
    player_warmth = 100
    
    print("Health:",player_health)
    print("Hunger:",player_hunger)
    print("Thirst:",player_thirst)
    print("Warmth:",player_warmth)

    #story: 1
    print("-------------------------------------------------------")
    print("BOOM")
    print("Your plane makes a loud, thunderous noise. It seems    ")
    print("as though one of the engines have blown out due to     ")
    print("flying in this intense blizzard.                       ")
    print("                                                       ")
    print("Before you know it, the plane is spiraling down        ")
    print("towards the icy tundra below. You ensure that your     ")
    print("seatbelt is fastened and you close your eyes, hoping   ")
    print("for the best.                                          ")
    print("-------------------------------------------------------")

    #player effects taken: 1
    print("Damage was taken during the crash. You are also exposed")
    print("to the weather conditions.                             ")
    player_health = 50

    #player stats: 2
    print("Health:",player_health)
    print("Hunger:",player_hunger)
    print("Thirst:",player_thirst)
    print("Warmth:",player_warmth)

    #story: 2
    print("-------------------------------------------------------")
    print("You wake up hanging from your seat on the plane.       ")
    print("The only thing keeping you from falling into the       ")
    print("flaming remains of the aircraft. What do you do? Type  ")
    print("the number besides the answer you would like to choose ")
    print("in order to make your decision. ex. 1 or 2             ")
    print("")
    print("1. You unbuckle the seat belt and try to land on a     ")
    print("small section of the destroyed plane that is not on    ")
    print("on fire.                                               ")
    print("")
    print("2. You look around and see if there is anyone else     ")
    print("around to help you first.                              ")
    print("-------------------------------------------------------")

    choice_prompt_1 = input("> ")

    #choice prompt 1 if statement
    if choice_prompt_1.lower() == ("1"):
        print("You successfully unbuckle the seat belt and fall  ")
        print("to the floor, just barely missing the flames.     ")
        print("-------------------------------------------------------")
        print("Health:",player_health)
        print("Hunger:",player_hunger)
        print("Thirst:",player_thirst)
        print("Warmth:",player_warmth)
        print("")
        print("What do you do next?")
        print("1. you leave the plane as soon as possible")
        print("")
        print("2. you search for survivors")
        print("-------------------------------------------------------")

        choice_prompt_3 = input("> ")

        #choice_prompt_3 if statement
        if choice_prompt_3.lower() == ("1"):
            print("you run out of the flaming aircraft and manage to")
            print("avoid getting burned at all before it went totally")
            print("in flames.")
            print("")
            survive_art()
            print("")
            print("Congrats! You survived the plane crash!")
            print("Thanks for playing!")

        elif choice_prompt_3.lower() == ("2"):
            print("You call out from your new place on the ground.   ")
            print("'Hello?!'")
            print("There is no answer. You soon realize that the     ")
            print("people that were on this plane are now probably   ")
            print("all dead.                                         ")
            print("")
            print("You then start thinking about your next move.     ")
            print("However, the flames have grown since you wasted   ")
            print("time calling for survivors.                       ")

            #player effects taken: 2
            print("you are slowly taking burn damage from the fire   ")
            player_health = 40

            print("Health:",player_health)
            print("Hunger:",player_hunger)
            print("Thirst:",player_thirst)
            print("Warmth:",player_warmth)

            print("-------------------------------------------------------")
            print("Your shirt is starting to catch fire! What do you do?  ")
            print("1. you try to pat out of the flames before it gets worse ")
            print("")
            print("2. you make a run for it")
            print("-------------------------------------------------------")

            choice_prompt_4 = input("> ")

            #choice_prompt_4 if statement
            if choice_prompt_4.lower() == ("1"):
                print("You manage to put out the patch of fire that had ")
                print("started on your sleeve, but while you were doing ")
                print("so, the rest of your clothes caught fire.        ")
                print("")
                player_health = 0
                print("Health:",player_health)
                print("Hunger:",player_hunger)
                print("Thirst:",player_thirst)
                print("Warmth: way too freakin' hot")
                print("")
                death_art()
                print("")
                print("Oh no! You burned to death! Sucks to suck I guess~")
            
            elif choice_prompt_4.lower() == ("2"):
                print("you run out of the flaming aircraft and throw ")
                print("yourself into a pile of snow, successfully putting ")
                print("out the fire.")
                print("")
                survive_art()
                print("")
                print("Congrats! You survived the plane crash!")
                print("Thanks for playing!")

            elif choice_prompt_4.lower() == ("quit"):
                print("Wow, what a loser! Can't handle a little cold? I didn't want")
                print("to hang out with you anyways! Later~                        ")
                sys.exit()
        
    elif choice_prompt_1.lower() == ("2"):
        print("You call out from your position on the seat.      ")
        print("'Hello?!'")
        print("There is no answer. You soon realize that the     ")
        print("people that were on this plane are now probably   ")
        print("all dead.                                         ")
        print("")
        print("You then go to unbuckle yourself and drop down on ")
        print("the floor.                                        ")
        print("However, the flames have grown since you wasted   ")
        print("time calling for survivors.                       ")

        #player effects taken: 2
        print("you drop down onto the ground, but you are slowly ")
        print("taking burn damage from the fire.                 ")
        player_health = 40

        print("Health:",player_health)
        print("Hunger:",player_hunger)
        print("Thirst:",player_thirst)
        print("Warmth:",player_warmth)

        print("-------------------------------------------------------")
        print("Your shirt is starting to catch fire! What do you do?  ")
        print("1. you try to pat out of the flames before it gets worse ")
        print("")
        print("2. you make a run for it")
        print("-------------------------------------------------------")

        choice_prompt_2 = input("> ")

        #choice_prompt_2 if statement
        if choice_prompt_2.lower() == ("1"):
            print("You manage to put out the patch of fire that had ")
            print("started on your sleeve, but while you were doing ")
            print("so, the rest of your clothes caught fire.        ")
            print("")
            player_health = 0
            print("Health:",player_health)
            print("Hunger:",player_hunger)
            print("Thirst:",player_thirst)
            print("Warmth: way too freakin' hot")
            print("")
            death_art()
            print("")
            print("Oh no! You burned to death! Sucks to suck I guess~")
            
        elif choice_prompt_2.lower() == ("2"):
            print("you run out of the flaming aircraft and throw ")
            print("yourself into a pile of snow, successfully putting ")
            print("out the fire.")
            print("")
            survive_art()
            print("")
            print("Congrats! You survived the plane crash!")
            print("Thanks for playing!")

        elif choice_prompt_1.lower() == ("quit"):
            print("Wow, what a loser! Can't handle a little cold? I didn't want")
            print("to hang out with you anyways! Later~                        ")
            sys.exit()
        
    elif choice_prompt_1.lower() == ("quit"):
        print("Wow, what a loser! Can't handle a little cold? I didn't want")
        print("to hang out with you anyways! Later~                        ")
        sys.exit()
        
#### Calling the methods ####
title_screen()

































