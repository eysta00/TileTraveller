#Eysteinn Örn Jónsson & Úlfur Örn Björnsson
# 17/9/19 - Assignment 8
'''
Birt á skjáinn eru áttinar sem notandi getur farið í
    Byður notenda um inntak fyrir áttina sem hann vill ferðast í (n, s, w, e).
        ef notandi slær inn ógilt inntak þá á að koma villa og notandi á að reyna aftur.
Þegar notandi kemst á endastað þá kemur á skjáinn að notandi hefur unnið og forritið hættir.

    Hver átt hækkar eða lækkar, x eða y gildið sem mun merkja staðsetningu notanda.
        Þegar x og y eru ákveðin gildi þá mun birta á skjáinn viðeigandi áttir sem notandi má fara í.
        (Þar sem sumar staðsetningar þurfa að skila sömu upplýsingum væri gott að gera sameiginlegt fall)
'''
#north + 1, south -1
#east + 3, west -3

direction_input = ""
position = 1

def Only_North(direction):
    print("You can travel: (N)orth.")
    return position + 1 

def North_South(direction):
    print("You can travel: (N)orth or (S)outh.")
    if direction == "n":
        return + 1
    elif direction == "s"
        return - 1

def North_East_South(direction):
    print("You can travel: (N)orth or (E)ast or (S)outh.")

def South_West(direction):
    print("You can travel: (S)outh or (W)est.")
    return 3, 1

def South_East(direction):
    print("You can travel: (E)ast or (S)outh.")
    return 2, 2

def West_East(direction):
    print("You can travel: (E)ast or (W)est.")


while True:

    direction_input = input("Direction: ").lower()
    while direction_input == "n", "s", "w", "e":
        if position == 1:
            position = Only_North()
        elif position == 2:
            position = North_East_South()
        elif position == 3:
            position = South_East()
        elif position == 4:
            position = Only_North()
        elif position == 5:
            position = South_West()
        elif position == 6:
            position = West_East()
        elif position == 8:
            position = North_South()
        elif position == 9:
            position = South_West()
        else: #position == 7
            print("Victory!")
            break
    else:
        print("Invalid direction")
