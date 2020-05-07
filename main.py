import pygame

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))



pygame.display.set_caption('Mühle Spiel - FHNW Programmieren')

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)



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
        message_to_screen("www.irgendetwas.ch", black, -30)


        button("spielen", 150, 500, 150, 50, green, light_green, action="spielen")
        button("Hauptmenü", 350, 500, 150, 50, yellow, light_yellow, action="Hauptmenü")
        button("verlassen", 550, 500, 150, 50, red, light_red, action="verlassen")

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
                playboard()

            if action == "Hauptmenü":
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


        button("spielen", 150, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 350, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 550, 500, 150, 50, red, light_red, action="verlassen")

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

        button("nochmals spielen", 150, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 350, 500, 100, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 550, 500, 150, 50, red, light_red, action="verlassen")

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

        button("nochmals spielen", 150, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 350, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 550, 500, 150, 50, red, light_red, action="verlassen")

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








# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

#Spielfeld
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

def muehle_erkennen():
    neue_muehle = 0
    if spielfeld[0] == spielfeld[1] == spielfeld[2] != "x" and alle_muehlen[0] == 0:
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



def place_and_remove():
    steinberg = 18
    aktueller_spieler = "w"

    while steinberg > 0:
        spieleingabe = int(input("Geben Sie ein Feld zwischen 1 und 24 an."))
        print(alle_muehlen)
        if spieleingabe <= 24:
            if spielfeld[spieleingabe-1] == "x":
                spielfeld[spieleingabe - 1] = aktueller_spieler
                steinberg = steinberg -1
                muehle_erkennen()
                if aktueller_spieler == "w":
                    aktueller_spieler = "b"
                    print(spielfeld)
                    print(spieleingabe)
                else:
                    aktueller_spieler = "w"
                    print(spielfeld)
                    print(spieleingabe)
            else:
                print("Platz bereits belegt, bitte einen anderes Feld auswählen.")
        else:
            print(spielfeld)
            print(spieleingabe)
            print("Bitte wähle einen Platz auf dem Spielfeld aus (1 bis 24)!")











def playboard():
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
        screen.fill((207, 185, 151))

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
        pygame.draw.rect(screen, (0, 0, 0), (200, 30, 600, 1))
        pygame.draw.rect(screen, (0, 0, 0), (800, 30, 1, 600))
        pygame.draw.rect(screen, (0, 0, 0), (200, 30, 1, 600))
        pygame.draw.rect(screen, (0, 0, 0), (200, 630, 600, 1))
        #mittlere Linie
        pygame.draw.rect(screen, (0, 0, 0), (300, 130, 400, 1))
        pygame.draw.rect(screen, (0, 0, 0), (700, 130, 1, 400))
        pygame.draw.rect(screen, (0, 0, 0), (300, 130, 1, 400))
        pygame.draw.rect(screen, (0, 0, 0), (300, 530, 400, 1))
        # innere Linie
        pygame.draw.rect(screen, (0, 0, 0), (400, 230, 200, 1))
        pygame.draw.rect(screen, (0, 0, 0), (600, 230, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (400, 230, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (400, 430, 200, 1))
        # innere Linie
        pygame.draw.rect(screen, (0, 0, 0), (500, 430, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (500, 30, 1, 200))
        pygame.draw.rect(screen, (0, 0, 0), (200, 330, 200, 1))
        pygame.draw.rect(screen, (0, 0, 0), (600, 330, 200, 1))

        # Inhalt von screen anzeigen.
        pygame.display.flip()



# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__playboard__':
    # Unsere Main-Funktion aufrufen.
    place_and_remove()

game_intro()

playboard()