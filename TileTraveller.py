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


pos_x = 1
pos_y = 1

def Only_North():
    print("You can travel: (N)orth.")
    return 1, 3

def North_South():
    print("You can travel: (N)orth or (S)outh.")

def North_East_South():
    print("You can travel: (N)orth or (E)ast or (S)outh.")

def South_West():
    print("You can travel: (S)outh or (W)est.")
    return 3, 1

def South_East():
    print("You can travel: (E)ast or (S)outh.")
    return 2, 2

def West_East():
    print("You can travel: (E)ast or (W)est.")


while True:
    if pos_x == 1 and pos_y == 1:
        pos_x, pos_y = Only_North()
    elif pos_x == 1 and pos_y == 2:
        pos_x, pos_y = North_East_South()
    elif pos_x == 1 and pos_y == 3:
        pos_x, pos_y = South_East()
    elif pos_x == 2 and pos_y == 1:
        pos_x, pos_y = Only_North()
    elif pos_x == 2 and pos_y == 2:
        pos_x, pos_y = South_West()
    elif pos_x == 2 and pos_y == 3:
        pos_x, pos_y = West_East()
    elif pos_x == 3 and pos_y == 2:
        pos_x, pos_y = North_South()
    elif pos_x == 3 and pos_y == 3:
        pos_x, pos_y = South_West()
    else:
        print("Victory!")
        break