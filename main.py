import pygame

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
aktueller_spieler = None
spielerw = 9
spielerb = 9



pygame.display.set_caption('Mühle Spiel - FHNW Programmieren')

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)
beige = (207, 185, 151)

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Link zu Regeln", green, -200, size="large")
        message_to_screen("https://www.spielezar.ch/blog/spielregeln/muehle-spielregeln", black, -30)


        button("spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button("Hauptmenü", 425, 500, 150, 50, yellow, light_yellow, action="Hauptmenü")
        button("verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()




def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "verlassen":
                pygame.quit()
                quit()

            if action == "Regeln":
                game_controls()

            if action == "spielen":
                playboard(action)

            if action == "Hauptmenü":
                game_intro()


    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def stein(text, x, y, width, height, inactive_color, active_color, action):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "verlassen":
                pygame.quit()
                quit()

            if action == "A1":
                spieleingabe = 1
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A2":
                spieleingabe = 2
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A3":
                spieleingabe = 3
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A4":
                spieleingabe = 4
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A5":
                spieleingabe = 5
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A6":
                spieleingabe = 6
                place_and_remove(aktueller_spieler, action, spieleingabe)
            if action == "A1" and neue_muehle == 1:
                spieleingabe = 1
                stein_entfernen(spieleingabe, action)



            if action == "spielen":
                playboard()

            if action == "A12":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: # Start Spiel durch Taste 'C'
                    intro = False
                elif event.key == pygame.K_q: # Abbruch Hauptmenü durch Taste 'Q'

                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Willkommen zu Mühle", green, -100, size="medium")
        message_to_screen("Das ist ein Mühle-Spiel", black, -30)
        message_to_screen("programmiert von Studenten der FHNW.", black, 10)


        button("spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 425, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()




def game_over(): #Muss noch angepasst werden!!
    game_over = True

    while game_over:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Game Over", green, -100, size="large")
        message_to_screen("You died.", black, -30)

        button("nochmals spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 425, 500, 100, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()




def you_win(): #Muss noch angepasst werden!!
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("You won!", green, -100, size="large")
        message_to_screen("Congratulations!", black, -30)

        button("nochmals spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 425, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()



def gameLoop():
    gameExit = False
    gameOver = False


    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

    pygame.quit()
    quit()







#Definition des Spielfeld

a1 = 'x'
a2 = 'x'
a3 = "x"
a4 = "x"
a5 = "x"
a6 = "x"
a7 = "x"
a8 = "x"
a9 = "x"
a10 = "x"
a11 = "x"
a12 = "x"
a13 = "x"
a14 = "x"
a15 = "x"
a16 = "x"
a17 = "x"
a18 = "x"
a19 = "x"
a20 = "x"
a21 = "x"
a22 = "x"
a23 = "x"
a24 = "x"

spielfeld = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24]


#Definition der Mühlen

muehle1 = 0
muehle2 = 0
muehle3 = 0
muehle4 = 0
muehle5 = 0
muehle6 = 0
muehle7 = 0
muehle8 = 0
muehle9 = 0
muehle10 = 0
muehle11 = 0
muehle12 = 0
muehle13 = 0
muehle14 = 0
muehle15 = 0
muehle16 = 0

alle_muehlen = [muehle1, muehle2, muehle3, muehle4, muehle5, muehle6, muehle7, muehle8, muehle9, muehle10, muehle11, muehle12, muehle13, muehle14, muehle15, muehle16]

"""
def muehle_erkennen():
    neue_muehle = 0
    if spielfeld[0] == spielfeld[1] == spielfeld[2] == aktueller_spieler and alle_muehlen[0] == 0:
        alle_muehlen[0] = 1
        neue_muehle = 1
        print("Neue Mühle 1")
    elif spielfeld[3] == spielfeld[4] == spielfeld[5] != "x" and alle_muehlen[1] == 0:
        alle_muehlen[1] = 1
        neue_muehle = 1
        print("Neue Mühla1e 2")
    elif spielfeld[3] == spielfeld[4] == spielfeld[5] != "x" and alle_muehlen[1] == 0:
        alle_muehlen[1] = 1
        neue_muehle = 1
        print("Neue Mühla1e 2")
    else:
        print("keine neue Mühle")

    while neue_muehle == 1:
        print(spielfeld)
        stein_entfernen = int(input("Sie dürfen einen Stein Enfernen, aktueller Spielstand siehe oben:\n"))
        if stein_entfernen <= 24:
            if stein_entfernen == 1:
                if alle_muehlen[0] == 0:
                    spielfeld[stein_entfernen-1] = "x"
                    neue_muehle = 0
                else:
                    print("Stein befindet sich in einer Mühle")
            elif stein_entfernen == 4:
                if alle_muehlen[1] == 0:
                    spielfeld[stein_entfernen - 1] = "x"
                    neue_muehle = 0
                else:
                    print("Stein befindet sich in einer Mühle")
            else:
                if muehle4 == 0:
                    spielfeld[stein_entfernen - 1] = "x"
                    neue_muehle = 0
                else:
                    print("Stein befindet sich in einer Mühele")
        else:
            print("Bitte wähle einen Platz auf dem Spielfeld aus (1 bis 24)!")

"""
def muehle_erkennen(aktueller_spieler, action):
    neue_muehle = 0
    if spielfeld[0] == spielfeld[1] == spielfeld[2] == aktueller_spieler and alle_muehlen[0] == 0:
        alle_muehlen[0] = 1
        neue_muehle = 1
        print("Neue Mühle 1")
    elif spielfeld[2] == spielfeld[14] == spielfeld[23] == aktueller_spieler and alle_muehlen[1] == 0:
        alle_muehlen[1] = 1
        neue_muehle = 1
        print("Neue Mühle 2")
    elif spielfeld[21] == spielfeld[22] == spielfeld[23] == aktueller_spieler and alle_muehlen[2] == 0:
        alle_muehlen[2] = 1
        neue_muehle = 1
        print("Neue Mühle 3")
    elif spielfeld[0] == spielfeld[9] == spielfeld[21] == aktueller_spieler and alle_muehlen[3] == 0:
        alle_muehlen[3] = 1
        neue_muehle = 1
        print("Neue Mühle 4")
    elif spielfeld[3] == spielfeld[4] == spielfeld[5] == aktueller_spieler and alle_muehlen[4] == 0:
        alle_muehlen[4] = 1
        neue_muehle = 1
        print("Neue Mühle 5")
    elif spielfeld[5] == spielfeld[13] == spielfeld[20] == aktueller_spieler and alle_muehlen[5] == 0:
        alle_muehlen[5] = 1
        neue_muehle = 1
        print("Neue Mühle 6")
    elif spielfeld[18] == spielfeld[19] == spielfeld[20] == aktueller_spieler and alle_muehlen[6] == 0:
        alle_muehlen[6] = 1
        neue_muehle = 1
        print("Neue Mühle 7")
    elif spielfeld[3] == spielfeld[10] == spielfeld[18] == aktueller_spieler and alle_muehlen[7] == 0:
        alle_muehlen[7] = 1
        neue_muehle = 1
        print("Neue Mühle 8")
    elif spielfeld[6] == spielfeld[7] == spielfeld[8] == aktueller_spieler and alle_muehlen[8] == 0:
        alle_muehlen[8] = 1
        neue_muehle = 1
        print("Neue Mühle 9")
    elif spielfeld[8] == spielfeld[12] == spielfeld[17] == aktueller_spieler and alle_muehlen[9] == 0:
        alle_muehlen[9] = 1
        neue_muehle = 1
        print("Neue Mühle 10")
    elif spielfeld[15] == spielfeld[16] == spielfeld[17] == aktueller_spieler and alle_muehlen[10] == 0:
        alle_muehlen[10] = 1
        neue_muehle = 1
        print("Neue Mühle 11")
    elif spielfeld[6] == spielfeld[11] == spielfeld[15] == aktueller_spieler and alle_muehlen[11] == 0:
        alle_muehlen[11] = 1
        neue_muehle = 1
        print("Neue Mühle 12")
    elif spielfeld[1] == spielfeld[4] == spielfeld[7] == aktueller_spieler and alle_muehlen[12] == 0:
        alle_muehlen[12] = 1
        neue_muehle = 1
        print("Neue Mühle 13")
    elif spielfeld[12] == spielfeld[13] == spielfeld[14] == aktueller_spieler and alle_muehlen[13] == 0:
        alle_muehlen[13] = 1
        neue_muehle = 1
        print("Neue Mühle 14 ")

    elif spielfeld[16] == spielfeld[19] == spielfeld[22] == aktueller_spieler and alle_muehlen[14] == 0:
        alle_muehlen[14] = 1
        neue_muehle = 1
        print("Neue Mühle 15")
    elif spielfeld[9] == spielfeld[10] == spielfeld[11] == aktueller_spieler and alle_muehlen[15] == 0:
        alle_muehlen[15] = 1
        neue_muehle = 1
        print("Neue Mühl1 16")
    else:
        print("keine neue Mühle")



def stein_entfernen(action, spieleingabe):
    while neue_muehle == 1:
        stein_entfernen = spieleingabe
        if stein_entfernen <= 24:
            if stein_entfernen == 1:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[3] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 2:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 3:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[1] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 4:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[4] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 5:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[4] == 0 and alle_muehlen[12] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 6:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[4] == 0 and alle_muehlen[5] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 7:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[11] == 0 and alle_muehlen[8] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 8:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[8] == 0 and alle_muehlen[12] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 9:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[4] == 0 and alle_muehlen[4] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 10:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[3] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 11:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 12:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[11] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 13:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[9] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 14:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[5] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 15:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[1] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 16:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[11] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 17:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 18:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[9] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 19:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[6] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 20:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[6] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 21:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[6] == 0 and alle_muehlen[5] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 22:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[3] == 0 and alle_muehlen[2] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 23:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[2] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")
            elif stein_entfernen == 24:
                if stein_entfernen != aktueller_spieler:
                    if stein_entfernen != "x":
                        if alle_muehlen[2] == 0 and alle_muehlen[1] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                        else:
                            print("Stein befindet sich in einer Mühle!")
                    else:
                        print("Dieses Feld ist nicht belegt!")
                else:
                    print("Dies ist dein eigener Stein, du Depp!!")





        else:
            print("Bitte wähle einen Platz auf dem Spielfeld aus (1 bis 24)!")

action = None

def place_and_remove(aktueller_spieler, action, spieleingabe):
    steinberg = 18
    aktueller_spieler = "w"
    """cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()"""
    # print(click)
    while steinberg > 0:
        """spieleingabe = int(input("Geben Sie ein Feld zwischen 1 und 24 an."))"""
        """if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))"""
        print(alle_muehlen)
        if spieleingabe <= 24:
            if spielfeld[spieleingabe-1] == "x":
                spielfeld[spieleingabe - 1] = aktueller_spieler
                steinberg = steinberg -1
                # mühle erkennen
                muehle_erkennen(aktueller_spieler, action)
#spieler wechsel
                if aktueller_spieler == "w":
                    aktueller_spieler = "b"
                    print(spielfeld)
                    print(spieleingabe)
                    action = None
                    playboard(action, aktueller_spieler)
                    pygame.display.update()
                else:
                    aktueller_spieler = "w"
                    print(spielfeld)
                    print(spieleingabe)
                    action = None
                    playboard(action, aktueller_spieler)
                    pygame.display.update()
            else:
                print("Platz bereits belegt, bitte einen anderes Feld auswählen.")
        else:
            print(spielfeld)
            print(spieleingabe)
            print("Bitte wähle einen Platz auf dem Spielfeld aus (1 bis 24)!")

def move_and_remove(aktueller_spieler, action):
    aktueller_spieler = "w"
    game = 0
    while game == 0:
        steinwaehlen = int(input("Wähle den gewünschten Stein aus! \n"))
        if spielfeld[steinwaehlen - 1] == aktueller_spieler:
            steinsetzen = int(input("Wo hin soll der Stein gelegt werden?"))
            if spielfeld[steinsetzen - 1] == "x":
                spielfeld[steinsetzen - 1] = aktueller_spieler
                spielfeld[steinwaehlen - 1] = "x"
                if aktueller_spieler == "w":
                    aktueller_spieler = "b"
                    print(spielfeld)
                    print(spieleingabe)
                else:
                    aktueller_spieler = "w"
                    print(spielfeld)
                    print(spieleingabe)

def playboard(action):
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Mühle Spiel - FHNW Programmieren")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()

    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)

        # screen-Surface Baige
        screen.fill(beige)

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False

            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        #ausserste linie
        pygame.draw.rect(screen, (0, 0, 0), (200, 90, 600, 1))
        pygame.draw.rect(screen, (0, 0, 0), (800, 90, 1, 600))
        pygame.draw.rect(screen, (0, 0, 0), (200, 90, 1, 600))
        pygame.draw.rect(screen, (0, 0, 0), (200, 690, 600, 1))
        #mittlere Linie
        pygame.draw.rect(screen, (0, 0, 0), (300, 190, 400, 1))
        pygame.draw.rect(screen, (0, 0, 0), (700, 190, 1, 400))
        pygame.draw.rect(screen, (0, 0, 0), (300, 190, 1, 400))
        pygame.draw.rect(screen, (0, 0, 0), (300, 590, 400, 1))
        # innere Linie
        pygame.draw.rect(screen, (0, 0, 0), (400, 290, 200, 1))
        pygame.draw.rect(screen, (0, 0, 0), (600, 290, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (400, 290, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (400, 490, 200, 1))
        # innere Linie
        pygame.draw.rect(screen, (0, 0, 0), (500, 490, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (500, 90, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (200, 390, 200, 1))
        pygame.draw.rect(screen, (0, 0, 0), (600, 390, 200, 1))

        action = None
        # Inhalt von screen anzeigen.
        pygame.display.flip()

        button("Hauptmenü", 20, 50, 150, 50, yellow, red, action="Hauptmenü")

        stein("A1", 185, 75, 30, 30, yellow, light_green, action="A1")  #A1
        stein("A2", 485, 75, 30, 30, yellow, light_green, action="A2")  #A2
        stein("A3", 785, 75, 30, 30, yellow, light_green, action="A3")  #A3
        stein("A4", 285, 175, 30, 30, yellow, light_green, action="A4")  #A4
        stein("A5", 485, 175, 30, 30, yellow, light_green, action="A5")  #A5
        stein("A6", 685, 175, 30, 30, yellow, light_green, action="A6")  #A6
        stein("A7", 385, 275, 30, 30, yellow, light_green, action="A7")  #A7
        stein("A8", 485, 275, 30, 30, yellow, light_green, action="A8")  #A8
        stein("A9", 585, 275, 30, 30, yellow, light_green, action="A9")  #A9
        stein("A10", 185, 375, 30, 30, yellow, light_green, action="drücken")  #A10
        stein("A11", 285, 375, 30, 30, yellow, light_green, action="drücken")  #A11
        stein("A12", 385, 375, 30, 30, yellow, light_green, action="drücken")  #A12
        stein("A13", 585, 375, 30, 30, yellow, light_green, action="drücken")  #A13
        stein("A14", 685, 375, 30, 30, yellow, light_green, action="drücken")  #A14
        stein("A15", 785, 375, 30, 30, yellow, light_green, action="drücken")  #A15
        stein("A16", 385, 475, 30, 30, yellow, light_green, action="drücken")  #A16
        stein("A17", 485, 475, 30, 30, yellow, light_green, action="drücken")  #A17
        stein("A18", 585, 475, 30, 30, yellow, light_green, action="drücken")  #A18
        stein("A19", 285, 575, 30, 30, yellow, light_green, action="drücken")  #A19
        stein("A20", 485, 575, 30, 30, yellow, light_green, action="drücken")  #A20
        stein("A21", 685, 575, 30, 30, yellow, light_green, action="drücken")  #A21
        stein("A22", 185, 675, 30, 30, yellow, light_green, action="drücken")  #A22
        stein("A23", 485, 675, 30, 30, yellow, light_green, action="drücken")  #A23
        stein("A24", 785, 675, 30, 30, yellow, light_green, action="drücken")  #A24


        pygame.display.update()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__playboard__':
    # Unsere Main-Funktion aufrufen.

    pygame.quit()
    quit()

game_intro()

playboard(action)
