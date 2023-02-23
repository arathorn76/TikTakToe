

def print_grid(status):
    print(status)
    for i in [0,3,6]:
            print(status[i],'|',status[i+1],'|',status[i+2])
            
def spielanfang():
    status = []
    for i in range(0,9):
        status.append('.')
    return status


fertig = False
zug = ''
spieler = 'X'
spielfeld = []
spielfeld = spielanfang()
    
while(fertig == False):

    print_grid(spielfeld)
        
    zug = input('Zeile + Spalte (z.B. 00 für oben links):')
        
    x = int(zug[0])
    y = int(zug[1])
        
    spielfeld[x+3*y] = spieler

    if spieler == 'X':
        spieler = 'O'
    else:
        spieler = 'X'
        
        