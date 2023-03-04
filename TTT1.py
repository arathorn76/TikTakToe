fertig = False
zug = ''
spieler = 'X'
spielfeld = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    
while(not fertig):

    for i in [0,3,6]:
            print(spielfeld[i],'|',spielfeld[i+1],'|',spielfeld[i+2])
    
    zug = input('Zeile + Spalte (z.B. 00 für oben links):')
        
    x = int(zug[0])
    y = int(zug[1])
        
    spielfeld[x+3*y] = spieler

    if spieler == 'X':
        spieler = 'O'
    else:
        spieler = 'X'
        