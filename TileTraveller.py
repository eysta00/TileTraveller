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
position = 1

# each tile has been assigned a value between 1 and 9. 
# Adding or subtracting 1 to the position is equivalent to moving up or down respectively.
# Adding or subtracting 3 to the position is equivalent to moving right or left respectively.
# If an invalid input is entered the function is run again and the user is asked for another input. (Recursion)

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
    user_input = input("Pull a lever (y/n): ").lower()
    if user_input == "y":
        coins += 1
        print("You received 1 coin, your total is now {}.".format(coins))
        return coins
    else:
        return coins
def Only_North(direction):
    if direction == "n": 
        return position + 1 
    else: 
        print("Not a valid direction!")
        print_available_dir("n")
        return Only_North(direction_input())

def North_South(direction): # North is adding 1 and south is subtracting 1
    if direction == "n":
        return position + 1
    elif direction == "s":
        return position - 1
    else: 
        print("Not a valid direction!")
        print_available_dir("ns")
        return North_South(direction_input())

def North_East_South(direction):
    if direction == "n":
        return position + 1
    elif direction == "e":
        return position + 3
    elif direction == "s":
        return position - 1
    else: 
        print("Not a valid direction!")
        print_available_dir("nes")
        return North_East_South(direction_input())

def South_West(direction):
    if direction == "s":
        return position - 1
    elif direction == "w":
        return position - 3
    else: 
        print("Not a valid direction!")
        print_available_dir("sw")
        return South_West(direction_input())

def South_East(direction):
    if direction == "s":
        return position - 1
    elif direction == "e":
        return position + 3
    else: 
        print("Not a valid direction!")
        print_available_dir("es")
        return South_East(direction_input())

def West_East(direction): # West is subtracting 3 and east is adding 3
    if direction == "w":
        return position - 3
    elif direction == "e":
        return position + 3
    else: 
        print("Not a valid direction!")
        print_available_dir("ew ")
        return West_East(direction_input())

def direction_input():
    direction_input = input("Direction: ").lower()
    return direction_input

# These if-else statements check the position and run their respective function.
coins = 0
loop_bool = True
while loop_bool:
    if position == 1:
        print_available_dir("n")
        position = Only_North(direction_input())   

    elif position == 2:
        coins = pull_lever(coins)
        print_available_dir("nes")
        position = North_East_South(direction_input())

    elif position == 3:
        print_available_dir("es")
        position = South_East(direction_input())

    elif position == 4:
        print_available_dir("n")
        position = Only_North(direction_input())

    elif position == 5:
        coins = pull_lever(coins)
        print_available_dir("sw")
        position = South_West(direction_input())

    elif position == 6:
        coins = pull_lever(coins)
        print_available_dir("ew")
        position = West_East(direction_input())

    elif position == 8:
        coins = pull_lever(coins)
        print_available_dir("ns")
        position = North_South(direction_input())

    elif position == 9:
        print_available_dir("sw")
        position = South_West(direction_input())

    else: #position == 7 # the only other possible position is 7
        print("Victory! Total coins {}.".format(coins))
        loop_input = input("Play again (y/n): ").lower()
        if loop_input == "y":
            position = 1
            coins = 0
        else:
            loop_bool = False
        # Victory has been achieved and the loop is terminated.