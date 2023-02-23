"""Einfaches TikTakToe für die Kommandozeile"""

import logging

#################################
### Definition von Funktionen ###
#################################
def ix(a, b): 
    """Berechne Index für 2D-Zugriff auf 1D-Liste"""
    return a + 3 * b

def print_grid(status):
    """Ausgabe des Spielfelds"""
    for i in [0, 3, 6]:
        print(status[i], '|', status[i + 1], '|', status[i + 2])


def spielanfang():
    """Initialisierung des Spielfelds"""
    status = []
    for i in range(0, 9):
        status.append('.')
    return status

def ist_fertig(feld):
    """Ermittlung für Spielende
    
    Wahr, wenn 3er-Reihe
    draw, wenn alle Felder gefüllt aber keine 3er-Reihe
    Falsch, wenn keine der beiden anderen Bedingungen erfüllt ist"""

    # senkrecht
    if feld[ix(0, 0)] == feld[ix(0, 1)] == feld[ix(0, 2)] and feld[ix(0, 0)] in ['X', 'O']:
        return True
    if feld[ix(1, 0)] == feld[ix(1, 1)] == feld[ix(1, 2)] and feld[ix(1, 0)] in ['X', 'O']:
        return True
    if feld[ix(2, 0)] == feld[ix(2, 1)] == feld[ix(2, 2)] and feld[ix(2, 0)] in ['X', 'O']:
        return True

    # waagrecht
    if feld[ix(0, 0)] == feld[ix(1, 0)] == feld[ix(2, 0)] and feld[ix(0, 0)] in ['X', 'O']:
        return True
    if feld[ix(0, 1)] == feld[ix(1, 1)] == feld[ix(2, 1)] and feld[ix(0, 1)] in ['X', 'O']:
        return True
    if feld[ix(0, 2)] == feld[ix(1, 2)] == feld[ix(2, 2)] and feld[ix(0, 2)] in ['X', 'O']:
        return True

    # diagonal
    if feld[ix(0, 0)] == feld[ix(1, 1)] == feld[ix(2, 2)] and feld[ix(0, 0)] in ['X', 'O']:
        return True
    if feld[ix(0, 2)] == feld[ix(2, 0)] == feld[ix(1, 1)] and feld[ix(1, 1)] in ['X', 'O']:
        return True

    # noch nicht alle Felder voll
    for i in range(0,9):
        if feld[i] == '.':
            return False

    # nix davon, also alle Felder voll und keine 3er-Reihe
    return 'draw'

def check_input(inp):
    """Zeichenweise Prüfung und Konvertierung der Inputs, 
    
    wenn gültiger Wert dann diesen als INT zurückgeben
    sonst -1"""
    if inp in ['0', '1', '2']: 
        return int(inp)
    else:
        logging.warning('Wert %s ungültig, muss 0, 1 oder 2 sein', inp)
        return -1
        
def naechster(spieler):
    """nächster Spieler"""
    if spieler == 'X':
        return 'O'
    else:
        return 'X'

##################################
### Hauptprogramm beginnt hier ###
##################################
if __name__ == '__main__':

    # logging.basicConfig(level = logging.DEBUG)

    fertig = False
    zug = ''
    spieler = 'X'
    spielfeld = spielanfang()

    while not fertig:

        print_grid(spielfeld)

        x = y = -1
        while x not in [0, 1, 2] or y not in [0, 1, 2]:
            zug = input('Zeile + Spalte (z.B. 00 für oben links); "qq" zum Beenden: ')
            logging.debug(zug)

            # Eingabe prüfen
            if len(zug) < 2: #FIXME Länge 1 reicht aus, wenn q oder Q eingegeben wurde
                logging.warning('Eingabe zu kurz: %s Zeichen, muss 2 Ziffern 0-2 sein', len(zug))
                continue

            if zug[0] in ['q', 'Q']:
                exit()

            x = check_input(zug[0])
            logging.debug('x = %s',x)

            y = check_input(zug[1])
            logging.debug('y = %s',y)

        # Wenn Zug möglich
        if spielfeld[x + 3 * y] != '.':
            logging.warning('Feld bereits belegt.')
            continue

        spielfeld[x + 3 * y] = spieler #Zug ausführen

        fertig = ist_fertig(spielfeld)

        if fertig == 'draw': print('Unentschieden')
        elif fertig: print('Gewinner: ', spieler)

        spieler = naechster(spieler)

    print_grid(spielfeld)
