import pygame

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

#Spielfeld
a1 = ['x']
a2 = ['x']
a3 = ["x"]
a4 = ["x"]
a5 = ["x"]
a6 = ["x"]
a7 = ["x"]
a8 = ["x"]
a9 = ["x"]
a10 = ["x"]
a11 = ["x"]
a12 = ["x"]
a13 = ["x"]
a14 = ["x"]
a15 = ["x"]
a16 = ["x"]
a17 = ["x"]
a18 = ["x"]
a19 = ["x"]
a20 = ["x"]
a21 = ["x"]
a22 = ["x"]
a23 = ["x"]
a24 = ["x"]

spielfeld = ['a1', 'a2', a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24]

"print (spielfeld)"

def place_and_remove():
    aktueller_spieler = 1
    test = False


    while test == False:
        spieleingabe = input("Geben Sie ein Feld zwischen a1 und a24 an.")
        if spieleingabe in spielfeld:
            if spieleingabe == "x":
                print(spieleingabe)
                spieleingabe = aktueller_spieler
                break
            else:
                print(spieleingabe)
                print("Platz bereits belegt, bitte einen anderes Feld auswählen.")
        else:
            print("Bitte wähle einen Platz auf dem Spielfeld aus (a1 bis a24), achte auf die Schreibweise!")
            break
    print(spielfeld)









def main():
    # Initialisieren aller Pygame-Module und
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))

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
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    place_and_remove()