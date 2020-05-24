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
blue = (0,0,255)

green = (34, 177, 76)
light_green = (0, 255, 0)
beige = (207, 185, 151)

blocksize = 30


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
        message_to_screen("https://www.spielezar.ch/blog/spielregeln/muehle-spielregeln", blue, -30)


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


        button("spielen", 200, 500, 150, 50, green, light_green, action="spielen")
        button("Regeln", 400, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button("verlassen", 600, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()




def playboard():
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Mühle Spiel - FHNW Programmieren")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Fragmentrate zu begrenzen.
    clock = pygame.time.Clock()


    schwarz1 = pygame.rect.Rect(80, 150, blocksize, blocksize)
    schwarz1_draging = False

    schwarz2 = pygame.rect.Rect(80, 200, blocksize, blocksize)
    schwarz2_draging = False

    schwarz3 = pygame.rect.Rect(80, 250, blocksize, blocksize)
    schwarz3_draging = False

    schwarz4 = pygame.rect.Rect(80, 300, blocksize, blocksize)
    schwarz4_draging = False

    schwarz5 = pygame.rect.Rect(80, 350, blocksize, blocksize)
    schwarz5_draging = False

    schwarz6 = pygame.rect.Rect(80, 400, blocksize, blocksize)
    schwarz6_draging = False

    schwarz7 = pygame.rect.Rect(80, 450, blocksize, blocksize)
    schwarz7_draging = False

    schwarz8 = pygame.rect.Rect(80, 500, blocksize, blocksize)
    schwarz8_draging = False

    schwarz9 = pygame.rect.Rect(80, 550, blocksize, blocksize)
    schwarz9_draging = False

    weiss1 = pygame.rect.Rect(45, 150, blocksize, blocksize)
    weiss1_draging = False

    weiss2 = pygame.rect.Rect(45, 200, blocksize, blocksize)
    weiss2_draging = False

    weiss3 = pygame.rect.Rect(45, 250, blocksize, blocksize)
    weiss3_draging = False

    weiss4 = pygame.rect.Rect(45, 300, blocksize, blocksize)
    weiss4_draging = False

    weiss5 = pygame.rect.Rect(45, 350, blocksize, blocksize)
    weiss5_draging = False

    weiss6 = pygame.rect.Rect(45, 400, blocksize, blocksize)
    weiss6_draging = False

    weiss7 = pygame.rect.Rect(45, 450, blocksize, blocksize)
    weiss7_draging = False

    weiss8 = pygame.rect.Rect(45, 500, blocksize, blocksize)
    weiss8_draging = False

    weiss9 = pygame.rect.Rect(45, 550, blocksize, blocksize)
    weiss9_draging = False


    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)

        # screen-Surface Baige
        screen.fill(beige)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#--------------------------------------------------------------    S1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz1.collidepoint(event.pos):
                        schwarz1_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz1.x - mouse_x
                        offset_y = schwarz1.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz1_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz1_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz1.x = mouse_x + offset_x
                    schwarz1.y = mouse_y + offset_y

 # --------------------------------------------------------------  S 2

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz2.collidepoint(event.pos):
                        schwarz2_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz2.x - mouse_x
                        offset_y = schwarz2.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz2_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz2_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz2.x = mouse_x + offset_x
                    schwarz2.y = mouse_y + offset_y

# --------------------------------------------------------------  S3

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz3.collidepoint(event.pos):
                        schwarz3_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz3.x - mouse_x
                        offset_y = schwarz3.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz3_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz3_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz3.x = mouse_x + offset_x
                    schwarz3.y = mouse_y + offset_y

 # --------------------------------------------------------------  S4

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz4.collidepoint(event.pos):
                        schwarz4_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz4.x - mouse_x
                        offset_y = schwarz4.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz4_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz4_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz4.x = mouse_x + offset_x
                    schwarz4.y = mouse_y + offset_y

# --------------------------------------------------------------  S5

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz5.collidepoint(event.pos):
                        schwarz5_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz5.x - mouse_x
                        offset_y = schwarz5.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz5_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz5_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz5.x = mouse_x + offset_x
                    schwarz5.y = mouse_y + offset_y

# -------------------------------------------------------------- S 6

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz6.collidepoint(event.pos):
                        schwarz6_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz6.x - mouse_x
                        offset_y = schwarz6.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz6_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz6_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz6.x = mouse_x + offset_x
                    schwarz6.y = mouse_y + offset_y

# --------------------------------------------------------------  S7

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz7.collidepoint(event.pos):
                        schwarz7_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz7.x - mouse_x
                        offset_y = schwarz7.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz7_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz7_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz7.x = mouse_x + offset_x
                    schwarz7.y = mouse_y + offset_y

# --------------------------------------------------------------  S8

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz8.collidepoint(event.pos):
                        schwarz8_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz8.x - mouse_x
                        offset_y = schwarz8.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz8_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz8_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz8.x = mouse_x + offset_x
                    schwarz8.y = mouse_y + offset_y

# --------------------------------------------------------------  S9

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if schwarz9.collidepoint(event.pos):
                        schwarz9_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = schwarz9.x - mouse_x
                        offset_y = schwarz9.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    schwarz9_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if schwarz9_draging:
                    mouse_x, mouse_y = event.pos
                    schwarz9.x = mouse_x + offset_x
                    schwarz9.y = mouse_y + offset_y

 # --------------------------------------------------------------  w1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss1.collidepoint(event.pos):
                        weiss1_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss1.x - mouse_x
                        offset_y = weiss1.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss1_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss1_draging:
                    mouse_x, mouse_y = event.pos
                    weiss1.x = mouse_x + offset_x
                    weiss1.y = mouse_y + offset_y

        # --------------------------------------------------------------  w2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss2.collidepoint(event.pos):
                        weiss2_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss2.x - mouse_x
                        offset_y = weiss2.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss2_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss2_draging:
                    mouse_x, mouse_y = event.pos
                    weiss2.x = mouse_x + offset_x
                    weiss2.y = mouse_y + offset_y
        # --------------------------------------------------------------  w3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss3.collidepoint(event.pos):
                        weiss3_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss3.x - mouse_x
                        offset_y = weiss3.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss3_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss3_draging:
                    mouse_x, mouse_y = event.pos
                    weiss3.x = mouse_x + offset_x
                    weiss3.y = mouse_y + offset_y
        # --------------------------------------------------------------  w4
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss4.collidepoint(event.pos):
                        weiss4_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss4.x - mouse_x
                        offset_y = weiss4.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss4_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss4_draging:
                    mouse_x, mouse_y = event.pos
                    weiss4.x = mouse_x + offset_x
                    weiss4.y = mouse_y + offset_y
        # --------------------------------------------------------------  w5
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss5.collidepoint(event.pos):
                        weiss5_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss5.x - mouse_x
                        offset_y = weiss5.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss5_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss5_draging:
                    mouse_x, mouse_y = event.pos
                    weiss5.x = mouse_x + offset_x
                    weiss5.y = mouse_y + offset_y
        # --------------------------------------------------------------  w6
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss6.collidepoint(event.pos):
                        weiss6_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss6.x - mouse_x
                        offset_y = weiss6.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss6_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss6_draging:
                    mouse_x, mouse_y = event.pos
                    weiss6.x = mouse_x + offset_x
                    weiss6.y = mouse_y + offset_y
        # --------------------------------------------------------------  w7
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss7.collidepoint(event.pos):
                        weiss7_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss7.x - mouse_x
                        offset_y = weiss7.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss7_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss7_draging:
                    mouse_x, mouse_y = event.pos
                    weiss7.x = mouse_x + offset_x
                    weiss7.y = mouse_y + offset_y
        # --------------------------------------------------------------  w8
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss8.collidepoint(event.pos):
                        weiss8_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss8.x - mouse_x
                        offset_y = weiss8.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss8_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss8_draging:
                    mouse_x, mouse_y = event.pos
                    weiss8.x = mouse_x + offset_x
                    weiss8.y = mouse_y + offset_y
        # --------------------------------------------------------------  w9

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if weiss9.collidepoint(event.pos):
                        weiss9_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = weiss9.x - mouse_x
                        offset_y = weiss9.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    weiss9_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if weiss9_draging:
                    mouse_x, mouse_y = event.pos
                    weiss9.x = mouse_x + offset_x
                    weiss9.y = mouse_y + offset_y


        screen.fill(beige)
        pygame.draw.rect(screen, black, schwarz1)
        pygame.draw.rect(screen, black, schwarz2)
        pygame.draw.rect(screen, black, schwarz3)
        pygame.draw.rect(screen, black, schwarz4)
        pygame.draw.rect(screen, black, schwarz5)
        pygame.draw.rect(screen, black, schwarz6)
        pygame.draw.rect(screen, black, schwarz7)
        pygame.draw.rect(screen, black, schwarz8)
        pygame.draw.rect(screen, black, schwarz9)

        pygame.draw.rect(screen, white, weiss1)
        pygame.draw.rect(screen, white, weiss2)
        pygame.draw.rect(screen, white, weiss3)
        pygame.draw.rect(screen, white, weiss4)
        pygame.draw.rect(screen, white, weiss5)
        pygame.draw.rect(screen, white, weiss6)
        pygame.draw.rect(screen, white, weiss7)
        pygame.draw.rect(screen, white, weiss8)
        pygame.draw.rect(screen, white, weiss9)

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

        button("Hauptmenü", 840, 80, 150, 50, beige, light_yellow, action="Hauptmenü")
        button("verlassen", 840, 220, 150, 50, beige, light_red, action="verlassen")
        button("restart", 840, 150, 150, 50, beige, light_green, action="spielen")
        button("Steine", 45, 80, 80, 50, beige, beige, action="")


        # Inhalt von screen anzeigen.
        pygame.display.flip()








# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__playboard__':
    # Unsere Main-Funktion aufrufen.
    place_and_remove()

    pygame.quit()
    quit()

game_intro()

playboard()




rectangle = pygame.rect.Rect(176, 134, 17, 17)
rectangle_draging = False

rectangle2 = pygame.rect.Rect(76, 134, 17, 17)
rectangle2_draging = False



running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y



        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle2.collidepoint(event.pos):
                    rectangle2_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle2.x - mouse_x
                    offset_y = rectangle2.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle2_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle2_draging:
                mouse_x, mouse_y = event.pos
                rectangle2.x = mouse_x + offset_x
                rectangle2.y = mouse_y + offset_y



    pygame.draw.rect(screen, black, rectangle)
    pygame.draw.rect(screen, black, rectangle2)

    pygame.display.update()




pygame.quit()