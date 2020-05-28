import pygame
import webbrowser



pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))

spieleingabe = 1
spielerw = 9
spielerb = 9
action = None
aktueller_spieler = "w"
neue_muehle = 0
steinberg = 18

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

spielsteine = [beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige]

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

        gameDisplay.fill(beige)
        message_to_screen("Link zu Regeln", green, -200, size="large")
        button(aktueller_spieler, "Link zu Regeln", 375, 350, 200, 50, beige, white, action="Link")
        #message_to_screen("https://www.spielezar.ch/blog/spielregeln/muehle-spielregeln", black, -30)


        button(aktueller_spieler, "spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button(aktueller_spieler, "Hauptmenü", 425, 500, 150, 50, yellow, light_yellow, action="Hauptmenü")
        button(aktueller_spieler, "verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()




def button(aktueller_spieler, text, x, y, width, height, inactive_color, active_color, action=None):
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
            if action == "Link":
                webbrowser.open("https://www.spielezar.ch/blog/spielregeln/muehle-spielregeln")

            if action == "spielen":
                playboard(action, aktueller_spieler, neue_muehle, spieleingabe)

            if action == "Hauptmenü":
                spielfeld[0:23] = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
                spielsteine[0:23] = [beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige, beige]
                steinebank[0:2] = [18, 9, 9]
                switch[0:2] = [0, 0, 0]
                mitteilung[0] = " "
                alle_muehlen[0:15] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                textanzeige[0] = "Steine platzieren"
                game_intro()
            if action == "Mühle_aufheben":
                aufheben(neue_muehle)
                spielerwechsel_erzwungen(neue_muehle, aktueller_spieler)
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def stein(spieleingabe, neue_muehle, aktueller_spieler, text, x, y, width, height, inactive_color, active_color, action):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "verlassen":
                pygame.quit()
                quit()
            if steinebank[0] == 0:
                #Steine bei move and remoe
                if switch[0] == 0:
                    if action == "A1" and neue_muehle == 0:
                        spieleingabe = 1
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A2" and neue_muehle == 0:
                        spieleingabe = 2
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A3" and neue_muehle == 0:
                        spieleingabe = 3
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A4" and neue_muehle == 0:
                        spieleingabe = 4
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A5" and neue_muehle == 0:
                        spieleingabe = 5
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A6" and neue_muehle == 0:
                        spieleingabe = 6
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A7" and neue_muehle == 0:
                        spieleingabe = 7
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A8" and neue_muehle == 0:
                        spieleingabe = 8
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A9" and neue_muehle == 0:
                        spieleingabe = 9
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A10" and neue_muehle == 0:
                        spieleingabe = 10
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A11" and neue_muehle == 0:
                        spieleingabe = 11
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A12" and neue_muehle == 0:
                        spieleingabe = 12
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A13" and neue_muehle == 0:
                        spieleingabe = 13
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A14" and neue_muehle == 0:
                        spieleingabe = 14
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A15" and neue_muehle == 0:
                        spieleingabe = 15
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A16" and neue_muehle == 0:
                        spieleingabe = 16
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A17" and neue_muehle == 0:
                        spieleingabe = 17
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A18" and neue_muehle == 0:
                        spieleingabe = 18
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A19" and neue_muehle == 0:
                        spieleingabe = 19
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A20" and neue_muehle == 0:
                        spieleingabe = 20
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A21" and neue_muehle == 0:
                        spieleingabe = 21
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A22" and neue_muehle == 0:
                        spieleingabe = 22
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A23" and neue_muehle == 0:
                        spieleingabe = 23
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    if action == "A24" and neue_muehle == 0:
                        spieleingabe = 24
                        switch[1] = spieleingabe
                        switch[0] = 1
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)

                    if action == "A1" and neue_muehle == 1:
                        stein_gegner = 1
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A2" and neue_muehle == 1:
                        stein_gegner = 2
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A3" and neue_muehle == 1:
                        stein_gegner = 3
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A4" and neue_muehle == 1:
                        stein_gegner = 4
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A5" and neue_muehle == 1:
                        stein_gegner = 5
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A6" and neue_muehle == 1:
                        stein_gegner = 6
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A7" and neue_muehle == 1:
                        stein_gegner = 7
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A8" and neue_muehle == 1:
                        stein_gegner = 8
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A9" and neue_muehle == 1:
                        stein_gegner = 9
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A10" and neue_muehle == 1:
                        stein_gegner = 10
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A11" and neue_muehle == 1:
                        stein_gegner = 11
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A12" and neue_muehle == 1:
                        stein_gegner = 12
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A13" and neue_muehle == 1:
                        stein_gegner = 13
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A14" and neue_muehle == 1:
                        stein_gegner = 14
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A15" and neue_muehle == 1:
                        stein_gegner = 15
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A16" and neue_muehle == 1:
                        stein_gegner = 16
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A17" and neue_muehle == 1:
                        stein_gegner = 17
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A18" and neue_muehle == 1:
                        stein_gegner = 18
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A19" and neue_muehle == 1:
                        stein_gegner = 19
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A20" and neue_muehle == 1:
                        stein_gegner = 20
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A21" and neue_muehle == 1:
                        stein_gegner = 21
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "22" and neue_muehle == 1:
                        stein_gegner = 22
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A23" and neue_muehle == 1:
                        stein_gegner = 23
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A24" and neue_muehle == 1:
                        stein_gegner = 24
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                else:
                    if action == "A1" and neue_muehle == 0:
                        spieleingabe = 1
                        switch[2] = spieleingabe
                        muehle_aufheben(aktueller_spieler, action, neue_muehle, spieleingabe)
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A2" and neue_muehle == 0:
                        spieleingabe = 2
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A3" and neue_muehle == 0:
                        spieleingabe = 3
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A4" and neue_muehle == 0:
                        spieleingabe = 4
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A5" and neue_muehle == 0:
                        spieleingabe = 5
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A6" and neue_muehle == 0:
                        spieleingabe = 6
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A7" and neue_muehle == 0:
                        spieleingabe = 7
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A8" and neue_muehle == 0:
                        spieleingabe = 8
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A9" and neue_muehle == 0:
                        spieleingabe = 9
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A10" and neue_muehle == 0:
                        spieleingabe = 10
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A11" and neue_muehle == 0:
                        spieleingabe = 11
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A12" and neue_muehle == 0:
                        spieleingabe = 12
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A13" and neue_muehle == 0:
                        spieleingabe = 13
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A14" and neue_muehle == 0:
                        spieleingabe = 14
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A15" and neue_muehle == 0:
                        spieleingabe = 15
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A16" and neue_muehle == 0:
                        spieleingabe = 16
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A17" and neue_muehle == 0:
                        spieleingabe = 17
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A18" and neue_muehle == 0:
                        spieleingabe = 18
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A19" and neue_muehle == 0:
                        spieleingabe = 19
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A20" and neue_muehle == 0:
                        spieleingabe = 20
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A21" and neue_muehle == 0:
                        spieleingabe = 21
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A22" and neue_muehle == 0:
                        spieleingabe = 22
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A23" and neue_muehle == 0:
                        spieleingabe = 23
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                    if action == "A24" and neue_muehle == 0:
                        spieleingabe = 24
                        switch[2] = spieleingabe
                        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)

                    if action == "A1" and neue_muehle == 1:
                        stein_gegner = 1
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A2" and neue_muehle == 1:
                        stein_gegner = 2
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A3" and neue_muehle == 1:
                        stein_gegner = 3
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A4" and neue_muehle == 1:
                        stein_gegner = 4
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A5" and neue_muehle == 1:
                        stein_gegner = 5
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A6" and neue_muehle == 1:
                        stein_gegner = 6
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A7" and neue_muehle == 1:
                        stein_gegner = 7
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A8" and neue_muehle == 1:
                        stein_gegner = 8
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A9" and neue_muehle == 1:
                        stein_gegner = 9
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A10" and neue_muehle == 1:
                        stein_gegner = 10
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A11" and neue_muehle == 1:
                        stein_gegner = 11
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A12" and neue_muehle == 1:
                        stein_gegner = 12
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A13" and neue_muehle == 1:
                        stein_gegner = 13
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A14" and neue_muehle == 1:
                        stein_gegner = 14
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A15" and neue_muehle == 1:
                        stein_gegner = 15
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A16" and neue_muehle == 1:
                        stein_gegner = 16
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A17" and neue_muehle == 1:
                        stein_gegner = 17
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A18" and neue_muehle == 1:
                        stein_gegner = 18
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A19" and neue_muehle == 1:
                        stein_gegner = 19
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A20" and neue_muehle == 1:
                        stein_gegner = 20
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A21" and neue_muehle == 1:
                        stein_gegner = 21
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "22" and neue_muehle == 1:
                        stein_gegner = 22
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A23" and neue_muehle == 1:
                        stein_gegner = 23
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)
                    if action == "A24" and neue_muehle == 1:
                        stein_gegner = 24
                        stein_entfernen(aktueller_spieler, action, neue_muehle, stein_gegner, spieleingabe)

            #Steine beim place and remove
            else:
                if action == "verlassen":
                    pygame.quit()
                    quit()
                if action == "A1" and neue_muehle == 0:
                    spieleingabe = 1
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A2" and neue_muehle == 0:
                    spieleingabe = 2
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A3" and neue_muehle == 0:
                    spieleingabe = 3
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A4" and neue_muehle == 0:
                    spieleingabe = 4
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A5" and neue_muehle == 0:
                    spieleingabe = 5
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A6" and neue_muehle == 0:
                    spieleingabe = 6
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A7" and neue_muehle == 0:
                    spieleingabe = 7
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A8" and neue_muehle == 0:
                    spieleingabe = 8
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A9" and neue_muehle == 0:
                    spieleingabe = 9
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A10" and neue_muehle == 0:
                    spieleingabe = 10
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A11" and neue_muehle == 0:
                    spieleingabe = 11
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A12" and neue_muehle == 0:
                    spieleingabe = 12
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A13" and neue_muehle == 0:
                    spieleingabe = 13
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A14" and neue_muehle == 0:
                    spieleingabe = 14
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A15" and neue_muehle == 0:
                    spieleingabe = 15
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A16" and neue_muehle == 0:
                    spieleingabe = 16
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A17" and neue_muehle == 0:
                    spieleingabe = 17
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A18" and neue_muehle == 0:
                    spieleingabe = 18
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A19" and neue_muehle == 0:
                    spieleingabe = 19
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A20" and neue_muehle == 0:
                    spieleingabe = 20
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A21" and neue_muehle == 0:
                    spieleingabe = 21
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A22" and neue_muehle == 0:
                    spieleingabe = 22
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A23" and neue_muehle == 0:
                    spieleingabe = 23
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                if action == "A24" and neue_muehle == 0:
                    spieleingabe = 24
                    place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)

                if action == "A1" and neue_muehle == 1:
                    stein_gegner = 1
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A2" and neue_muehle == 1:
                    stein_gegner = 2
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A3" and neue_muehle == 1:
                    stein_gegner = 3
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A4" and neue_muehle == 1:
                    stein_gegner = 4
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A5" and neue_muehle == 1:
                    stein_gegner = 5
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A6" and neue_muehle == 1:
                    stein_gegner = 6
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A7" and neue_muehle == 1:
                    stein_gegner = 7
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A8" and neue_muehle == 1:
                    stein_gegner = 8
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A9" and neue_muehle == 1:
                    stein_gegner = 9
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A10" and neue_muehle == 1:
                    stein_gegner = 10
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A11" and neue_muehle == 1:
                    stein_gegner = 11
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A12" and neue_muehle == 1:
                    stein_gegner = 12
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A13" and neue_muehle == 1:
                    stein_gegner = 13
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A14" and neue_muehle == 1:
                    stein_gegner = 14
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A15" and neue_muehle == 1:
                    stein_gegner = 15
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A16" and neue_muehle == 1:
                    stein_gegner = 16
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A17" and neue_muehle == 1:
                    stein_gegner = 17
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A18" and neue_muehle == 1:
                    stein_gegner = 18
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A19" and neue_muehle == 1:
                    stein_gegner = 19
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A20" and neue_muehle == 1:
                    stein_gegner = 20
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A21" and neue_muehle == 1:
                    stein_gegner = 21
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "22" and neue_muehle == 1:
                    stein_gegner = 22
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A23" and neue_muehle == 1:
                    stein_gegner = 23
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)
                if action == "A24" and neue_muehle == 1:
                    stein_gegner = 24
                    stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe)



    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def aufheben(neue_muehle):
    neue_muehle = 0
    mitteilung[0] = " "


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

        gameDisplay.fill(beige)
        message_to_screen("Willkommen zu Mühle", green, -100, size="medium")
        message_to_screen("Das ist ein Mühle-Spiel", black, -30)
        message_to_screen("programmiert von Studenten der FHNW.", black, 10)
        message_to_screen("© by Sandro Michel, Lorenz Wyssmann, Michael Klaus, Fabian Gürtler", black, 350)

        button(aktueller_spieler, "spielen", 225, 500, 150, 50, green, light_green, action="spielen")
        button(aktueller_spieler, "Regeln", 425, 500, 150, 50, yellow, light_yellow, action="Regeln")
        button(aktueller_spieler, "verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

        pygame.display.update()

def you_win():
    if steinebank[1] < 3:
        win = True

        while win:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(beige)
            message_to_screen("Weiss hat gewonnen!", green, -100, size="large")
            message_to_screen("Congratulations!", black, 30)

            button(aktueller_spieler, "Erneut spielen", 220, 500, 160, 50, green, light_green, action="Hauptmenü")
            button(aktueller_spieler, "Regeln", 425, 500, 150, 50, yellow, light_yellow, action="Regeln")
            button(aktueller_spieler, "verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

            pygame.display.update()
    if steinebank[2] < 3:
        win = True

        while win:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(beige)
            message_to_screen("Schwarz hat gewonnen!", green, -100, size="large")
            message_to_screen("Congratulations!", black, -30)

            button(aktueller_spieler, "Erneut spielen", 220, 500, 160, 50, green, light_green, action="Hauptmenü")
            button(aktueller_spieler, "Regeln", 425, 500, 150, 50, yellow, light_yellow, action="Regeln")
            button(aktueller_spieler, "verlassen", 625, 500, 150, 50, red, light_red, action="verlassen")

            pygame.display.update()

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

spielfeld = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24,]


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
#Definition von diversen Listen
steineberg = 18
spieler1 = 4
spieler2 = 4
steinebank = [8, spieler1, spieler2]
switch = [0, 0, 0]
textanzeige = ["Steine platzieren", " ", "Weiss am Zug"]
mitteilung = [" "]


def muehle_erkennen(aktueller_spieler, action, neue_muehle, spieleingabe):
    neue_muehle = 0
    if spielfeld[0] == spielfeld[1] == spielfeld[2] == aktueller_spieler and alle_muehlen[0] == 0:
        alle_muehlen[0] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"

        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[2] == spielfeld[14] == spielfeld[23] == aktueller_spieler and alle_muehlen[1] == 0:
        alle_muehlen[1] = 1
        neue_muehle = 1

        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[21] == spielfeld[22] == spielfeld[23] == aktueller_spieler and alle_muehlen[2] == 0:
        alle_muehlen[2] = 1
        neue_muehle = 1

        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[0] == spielfeld[9] == spielfeld[21] == aktueller_spieler and alle_muehlen[3] == 0:
        alle_muehlen[3] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[3] == spielfeld[4] == spielfeld[5] == aktueller_spieler and alle_muehlen[4] == 0:
        alle_muehlen[4] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[5] == spielfeld[13] == spielfeld[20] == aktueller_spieler and alle_muehlen[5] == 0:
        alle_muehlen[5] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[18] == spielfeld[19] == spielfeld[20] == aktueller_spieler and alle_muehlen[6] == 0:
        alle_muehlen[6] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[3] == spielfeld[10] == spielfeld[18] == aktueller_spieler and alle_muehlen[7] == 0:
        alle_muehlen[7] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[6] == spielfeld[7] == spielfeld[8] == aktueller_spieler and alle_muehlen[8] == 0:
        alle_muehlen[8] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[8] == spielfeld[12] == spielfeld[17] == aktueller_spieler and alle_muehlen[9] == 0:
        alle_muehlen[9] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[15] == spielfeld[16] == spielfeld[17] == aktueller_spieler and alle_muehlen[10] == 0:
        alle_muehlen[10] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[6] == spielfeld[11] == spielfeld[15] == aktueller_spieler and alle_muehlen[11] == 0:
        alle_muehlen[11] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[1] == spielfeld[4] == spielfeld[7] == aktueller_spieler and alle_muehlen[12] == 0:
        alle_muehlen[12] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[12] == spielfeld[13] == spielfeld[14] == aktueller_spieler and alle_muehlen[13] == 0:
        alle_muehlen[13] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[16] == spielfeld[19] == spielfeld[22] == aktueller_spieler and alle_muehlen[14] == 0:
        alle_muehlen[14] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    elif spielfeld[9] == spielfeld[10] == spielfeld[11] == aktueller_spieler and alle_muehlen[15] == 0:
        alle_muehlen[15] = 1
        neue_muehle = 1
        mitteilung[0] = "Du darfst einen Stein entfernen"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)


def muehle_aufheben(aktueller_spieler, aciton, neue_muhle, spieleingabe):
    if switch[1] == 1:
        alle_muehlen[0] = 0
        alle_muehlen[3] = 0
    elif switch[1] == 2:
        alle_muehlen[0] = 0
        alle_muehlen[12] = 0
    elif switch[1] == 3:
        alle_muehlen[0] = 0
        alle_muehlen[1] = 0
    elif switch[1] == 4:
        alle_muehlen[4] = 0
        alle_muehlen[7] = 0
    elif switch[1] == 5:
        alle_muehlen[4] = 0
        alle_muehlen[12] = 0
    elif switch[1] == 6:
        alle_muehlen[4] = 0
        alle_muehlen[5] = 0
    elif switch[1] == 7:
        alle_muehlen[8] = 0
        alle_muehlen[11] = 0
    elif switch[1] == 8:
        alle_muehlen[8] = 0
        alle_muehlen[12] = 0
    elif switch[1] == 9:
        alle_muehlen[8] = 0
        alle_muehlen[9] = 0
    elif switch[1] == 10:
        alle_muehlen[3] = 0
        alle_muehlen[15] = 0
    elif switch[1] == 11:
        alle_muehlen[7] = 0
        alle_muehlen[15] = 0
    elif switch[1] == 12:
        alle_muehlen[15] = 0
        alle_muehlen[11] = 0
    elif switch[1] == 13:
        alle_muehlen[9] = 0
        alle_muehlen[13] = 0
    elif switch[1] == 14:
        alle_muehlen[5] = 0
        alle_muehlen[13] = 0
    elif switch[1] == 15:
        alle_muehlen[1] = 0
        alle_muehlen[13] = 0
    elif switch[1] == 16:
        alle_muehlen[10] = 0
        alle_muehlen[11] = 0
    elif switch[1] == 17:
        alle_muehlen[10] = 0
        alle_muehlen[14] = 0
    elif switch[1] == 18:
        alle_muehlen[9] = 0
        alle_muehlen[10] = 0
    elif switch[1] == 19:
        alle_muehlen[6] = 0
        alle_muehlen[7] = 0
    elif switch[1] == 20:
        alle_muehlen[6] = 0
        alle_muehlen[14] = 0
    elif switch[1] == 21:
        alle_muehlen[6] = 0
        alle_muehlen[5] = 0
    elif switch[1] == 22:
        alle_muehlen[2] = 0
        alle_muehlen[3] = 0
    elif switch[1] == 23:
        alle_muehlen[2] = 0
        alle_muehlen[14] = 0
    elif switch[1] == 24:
        alle_muehlen[1] = 0
        alle_muehlen[2] = 0

def spielerwechsel_erzwungen(neue_muehle, aktueller_spieler):
    if aktueller_spieler == "w":
        aktueller_spieler = "b"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    else:
        aktueller_spieler = "w"
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)

def spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe):
    if aktueller_spieler == "w":
        aktueller_spieler = "b"
        steinebank[1] = steinebank[1] -1
        you_win()
        action = None
        pygame.display.update()
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
    else:
        aktueller_spieler = "w"
        steinebank[2] = steinebank[2] - 1
        you_win()
        action = None
        pygame.display.update()
        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)

def einfaerben(aktueller_spieler, neue_muehle, spieleingabe):

    if steinebank[0] == 0:
        if aktueller_spieler == "w":
            spielsteine[switch[2] - 1] = white
            spielsteine[switch[1] - 1] = beige
            aktueller_spieler = "b"
            pygame.display.update()
        else:
            spielsteine[switch[2] - 1] = black
            spielsteine[switch[1] - 1] = beige
            aktueller_spieler = "w"
            pygame.display.update()
    else:
        if aktueller_spieler == "w":
            spielsteine[spieleingabe - 1] = white
            aktueller_spieler = "b"
            pygame.display.update()
        else:
            spielsteine[spieleingabe - 1] = black
            aktueller_spieler = "w"
            pygame.display.update()
def stein_entfernen(aktueller_spieler,action, neue_muehle, stein_gegner, spieleingabe):
    while neue_muehle == 1:
        beige = (207,185, 151)
        steinberg = 18
        stein_entfernen = int(stein_gegner)
        print(stein_gegner)
        if stein_entfernen <= 24:
            if stein_entfernen == 1:
                if spielfeld[(stein_entfernen - 1)] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[3] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            spielsteine[stein_entfernen - 1] = beige
                            pygame.display.update()
                            neue_muehle = 0
                            if steinebank[0] > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            print("Stein befindet sich in einer Mühle!")
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 2:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 3:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[0] == 0 and alle_muehlen[1] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 4:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[4] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 5:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[4] == 0 and alle_muehlen[12] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 6:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[4] == 0 and alle_muehlen[5] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 7:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[11] == 0 and alle_muehlen[8] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 8:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[8] == 0 and alle_muehlen[12] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 9:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[8] == 0 and alle_muehlen[9] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 10:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[3] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 11:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 12:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[11] == 0 and alle_muehlen[15] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 13:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[9] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 14:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[5] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 15:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[1] == 0 and alle_muehlen[13] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 16:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[11] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 17:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 18:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[10] == 0 and alle_muehlen[9] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 19:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[7] == 0 and alle_muehlen[6] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 20:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[6] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 21:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[6] == 0 and alle_muehlen[5] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 22:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[3] == 0 and alle_muehlen[2] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 23:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[2] == 0 and alle_muehlen[14] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            elif stein_entfernen == 24:
                if spielfeld[stein_entfernen - 1] != aktueller_spieler:
                    if spielfeld[stein_entfernen - 1] != "x":
                        if alle_muehlen[2] == 0 and alle_muehlen[1] == 0:
                            spielfeld[stein_entfernen - 1] = "x"
                            neue_muehle = 0
                            spielsteine[stein_entfernen - 1] = beige
                            if steinberg > 0:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                            else:
                                spielerwechsel(aktueller_spieler, neue_muehle, spieleingabe)
                                move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
                        else:
                            mitteilung[0] = "Stein befindet sich in einer Mühle!"
                            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                    else:
                        mitteilung[0] = "Dieses Feld ist nicht belegt!"
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    mitteilung[0] = "Dies ist dein eigener Stein, du Depp!!"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            else:
                print("Bitte wähle einen Platz auf dem Spielfeld aus (1 bis 24)!")
                playboard(action, aktueller_spieler, neue_muehle, spieleingabe)


def place_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe):
    mitteilung[0] = " "
    white = (255, 255, 255)
    black = (0, 0, 0)

    if steinebank[0] == 0:
        move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe)
    else:

        while steinebank[0] > 0:
            if spieleingabe <= 24:
                if spielfeld[spieleingabe-1] == "x":
                    spielfeld[spieleingabe - 1] = aktueller_spieler
                    einfaerben(aktueller_spieler, neue_muehle, spieleingabe)
                    steinebank[0] = steinebank[0] - 1
                    # mühle erkennen
                    muehle_erkennen(aktueller_spieler, action, neue_muehle, spieleingabe)
                    #spieler wechsel
                    if aktueller_spieler == "w":
                        aktueller_spieler = "b"
                        action = None
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                        pygame.display.update()
                    else:
                        aktueller_spieler = "w"
                        action = None
                        playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                        pygame.display.update()
                else:
                    mitteilung[0] = "Platz bereits belegt, bitte einen anderes Feld auswählen."
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            else:
                mitteilung[0] ="Bitte wähle einen Platz auf dem Spielfeld aus !"
                playboard(action, aktueller_spieler, neue_muehle)

def move_and_remove(aktueller_spieler, action, neue_muehle, spieleingabe):
    textanzeige[0] = "Steine schieben"
    mitteilung[0] = " "
    pygame.display.update()
    game = 0
    while game == 0:
        if spielfeld[switch[1]-1] == aktueller_spieler:
            if spielfeld[switch[2]-1] == "x":
                spielfeld[switch[1] - 1] = "x"
                spielfeld[switch[2]-1] = aktueller_spieler
                einfaerben(aktueller_spieler, neue_muehle, spieleingabe)
                switch[0] = 0
                muehle_erkennen(aktueller_spieler, action, neue_muehle, spieleingabe)

                if aktueller_spieler == "w":
                    aktueller_spieler = "b"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
                else:
                    aktueller_spieler = "w"
                    playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
            else:
                mitteilung[0] = "Dieses Feld ist bereits belegt!"
                switch[0] = 0
                playboard(action, aktueller_spieler, neue_muehle, spieleingabe)

        else:
            mitteilung[0] = "Du kannst nur eigene Steine schieben"
            switch[0] = 0
            playboard(action, aktueller_spieler, neue_muehle, spieleingabe)


def playboard(action, aktueller_spieler, neue_muehle, spieleingabe):
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
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

        button(aktueller_spieler, "Hauptmenü", 20, 75, 150, 50, green, light_green, action="Hauptmenü")
        if steinebank[0] == 0:
            textanzeige[0] = "Steine schieben"
        if neue_muehle == 1:
            textanzeige[1] = "Mühle!"
        else:
            textanzeige[1] = " "
        if aktueller_spieler == "w":
            textanzeige[2] = "Weiss am Zug"
        else:
            textanzeige[2] = "Schwarz am Zug"

        button(aktueller_spieler, textanzeige[0], 240, 20, 200, 50, beige, beige, action="")
        button(aktueller_spieler, textanzeige[1], 400, 365, 200, 50, beige, beige, action="")
        button(aktueller_spieler, textanzeige[2], 540, 20, 200, 50, beige, beige, action="")
        button(aktueller_spieler, mitteilung[0], 20, 720, 880, 50, beige, beige, action="")

        button(aktueller_spieler, "Patt", 20, 150, 150, 50, green, light_green, action="Mühle_aufheben")

        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 185, 75, 30, 30, spielsteine[0], light_green, action="A1")  #A1
        stein(spieleingabe, neue_muehle, aktueller_spieler,"O", 485, 75, 30, 30, spielsteine[1], light_green, action="A2")  #A2
        stein(spieleingabe, neue_muehle, aktueller_spieler,"O", 785, 75, 30, 30, spielsteine[2], light_green, action="A3")  #A3
        stein(spieleingabe, neue_muehle, aktueller_spieler,"O", 285, 175, 30, 30, spielsteine[3], light_green, action="A4")  #A4
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 485, 175, 30, 30, spielsteine[4], light_green, action="A5")  #A5
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 685, 175, 30, 30, spielsteine[5], light_green, action="A6")  #A6
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 385, 275, 30, 30, spielsteine[6], light_green, action="A7")  #A7
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 485, 275, 30, 30, spielsteine[7], light_green, action="A8")  #A8
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 585, 275, 30, 30, spielsteine[8], light_green, action="A9")  #A9
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 185, 375, 30, 30, spielsteine[9], light_green, action="A10")  #A10
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 285, 375, 30, 30, spielsteine[10], light_green, action="A11")  #A11
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 385, 375, 30, 30, spielsteine[11], light_green, action="A12")  #A12
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 585, 375, 30, 30, spielsteine[12], light_green, action="A13")  #A13
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 685, 375, 30, 30, spielsteine[13], light_green, action="A14")  #A14
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 785, 375, 30, 30, spielsteine[14], light_green, action="A15")  #A15
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 385, 475, 30, 30, spielsteine[15], light_green, action="A16")  #A16
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 485, 475, 30, 30, spielsteine[16], light_green, action="A17")  #A17
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 585, 475, 30, 30, spielsteine[17], light_green, action="A18")  #A18
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 285, 575, 30, 30, spielsteine[18], light_green, action="A19")  #A19
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 485, 575, 30, 30, spielsteine[19], light_green, action="A20")  #A20
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 685, 575, 30, 30, spielsteine[20], light_green, action="A21")  #A21
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 185, 675, 30, 30, spielsteine[21], light_green, action="A22")  #A22
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 485, 675, 30, 30, spielsteine[22], light_green, action="A23")  #A23
        stein(spieleingabe, neue_muehle, aktueller_spieler, "O", 785, 675, 30, 30, spielsteine[23], light_green, action="A24")  #A24

        pygame.display.update()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__playboard__':
    # Unsere Main-Funktion aufrufen.

    pygame.quit()
    quit()

game_intro()

playboard(action, aktueller_spieler, neue_muehle, spieleingabe)
