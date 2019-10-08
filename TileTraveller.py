# Eysteinn Örn Jónsson & Úlfur Örn Björnsson
# 17/9/19 - Assignment 8
# https://github.com/eysta00/TileTraveller
'''
Birt á skjáinn eru áttinar sem notandi getur farið í
    Byður notenda um inntak fyrir áttina sem hann vill ferðast í (n, s, w, e).
        ef notandi slær inn ógilt inntak þá á að koma villa og notandi á að reyna aftur.
Þegar notandi kemst á endastað þá kemur á skjáinn að notandi hefur unnið og forritið hættir.

    Hver átt hækkar eða lækkar, x eða y gildið sem mun merkja staðsetningu notanda.
        Þegar x og y eru ákveðin gildi þá mun birta á skjáinn viðeigandi áttir sem notandi má fara í.
        (Þar sem sumar staðsetningar þurfa að skila sömu upplýsingum væri gott að gera sameiginlegt fall)
'''


# each tile has been assigned a value between 1 and 9. 
# Adding or subtracting 1 to the position is equivalent to moving up or down respectively.
# Adding or subtracting 3 to the position is equivalent to moving right or left respectively.
# If an invalid input is entered the function is run again and the user is asked for another input. (Recursion)

import random

def print_available_dir(available_dir):
    ''' The function takes in a string and prints out the possible directions '''
    print("You can travel:", end=" ")
    for c in available_dir:
        if c == "n":
            print("(N)orth", end="")
        elif c == "e":
            print("(E)ast", end="")
        elif c == "s":
            print("(S)outh", end="")
        elif c == "w":
            print("(W)est", end="")
        if c != available_dir[-1]:
            print(" or ", end="")
    print(".")

def pull_lever(coins):
    ''' The function takes in a user input or a random choice is made, if yes then
    you get a coin if no you dont get a coin and returns coins '''
    # user_input = input("Pull a lever (y/n): ").lower()
    user_input = random.choice("yn")
    print("Pull a lever (y/n):", user_input)
    if user_input == "y":
        coins += 1
        print("You received 1 coin, your total is now {}.".format(coins))
        return coins
    else:
        return coins

def Only_North(direction, valid_moves): # Valid moves is in all direction functions
    # and one is added each time the function is called, this counts all valid and invalid movese.
    valid_moves += 1
    if direction == "n": 
        return position + 1, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("n")
        return Only_North(direction_input(), valid_moves)

def North_South(direction, valid_moves): # North is adding 1 and south is subtracting 1
    valid_moves += 1
    if direction == "n":
        return position + 1, valid_moves
    elif direction == "s":
        return position - 1, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("ns")
        return North_South(direction_input(), valid_moves)

def North_East_South(direction, valid_moves):
    valid_moves += 1
    if direction == "n":
        return position + 1, valid_moves
    elif direction == "e":
        return position + 3, valid_moves
    elif direction == "s":
        return position - 1, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("nes")
        return North_East_South(direction_input(), valid_moves)

def South_West(direction, valid_moves):
    valid_moves += 1
    if direction == "s":
        return position - 1, valid_moves
    elif direction == "w":
        return position - 3, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("sw")
        return South_West(direction_input(), valid_moves)

def South_East(direction, valid_moves):
    valid_moves += 1
    if direction == "s":
        return position - 1, valid_moves
    elif direction == "e":
        return position + 3, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("es")
        return South_East(direction_input(), valid_moves)

def West_East(direction, valid_moves): # West is subtracting 3 and east is adding 3
    valid_moves += 1
    if direction == "w":
        return position - 3, valid_moves
    elif direction == "e":
        return position + 3, valid_moves
    else: 
        print("Not a valid direction!")
        print_available_dir("ew")
        return West_East(direction_input(), valid_moves)

def direction_input():
    # direction_input = input("Direction: ").lower()
    direction_input = random.choice("nesw")
    print("Direction:", direction_input)
    return direction_input


seed_input = int(input("Input seed: "))
random.seed(seed_input)
position = 1
coins = 0
valid_moves = 0
loop_bool = True
# These if-else statements check the position and run their respective function.
while loop_bool:
    
    if position == 1:
        print_available_dir("n")
        position, valid_moves = Only_North(direction_input(), valid_moves)   

    elif position == 2:
        coins = pull_lever(coins)
        print_available_dir("nes")
        position, valid_moves = North_East_South(direction_input(), valid_moves)

    elif position == 3:
        print_available_dir("es")
        position, valid_moves = South_East(direction_input(), valid_moves)

    elif position == 4:
        print_available_dir("n")
        position, valid_moves = Only_North(direction_input(), valid_moves)

    elif position == 5:
        coins = pull_lever(coins)
        print_available_dir("sw")
        position, valid_moves = South_West(direction_input(), valid_moves)

    elif position == 6:
        coins = pull_lever(coins)
        print_available_dir("ew")
        position, valid_moves = West_East(direction_input(), valid_moves)

    elif position == 8:
        coins = pull_lever(coins)
        print_available_dir("ns")
        position, valid_moves = North_South(direction_input(), valid_moves)

    elif position == 9:
        print_available_dir("sw")
        position, valid_moves = South_West(direction_input(), valid_moves)

    else: #position == 7 # the only other possible position is 7
        print("Victory! Total coins {}. Moves {}.".format(coins,valid_moves))
        loop_input = input("Play again (y/n): ").lower()
        if loop_input == "y":
            position = 1
            coins = 0
        else:
            loop_bool = False
        # Victory has been achieved and the loop is terminated.