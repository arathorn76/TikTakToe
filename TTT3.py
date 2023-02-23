

def print_grid(status):
    print(status)
    for i in [0,3,6]:
            print(status[i],'|',status[i+1],'|',status[i+2])
            
def spielanfang():
    status = []
    for i in range(0,9):
        status.append('.')
    return status

def istFertig(feld):
    #senkrecht
    if feld[0+3*0] == feld[0+3*1] and feld[0+3*0] == feld[0+3*2] and feld[0+3*0] in ['X','O']:
        return True
    if feld[1+3*0] == feld[1+3*1] and feld[1+3*0] == feld[1+3*2] and feld[1+3*0] in ['X','O']:
        return True
    if feld[2+3*0] == feld[2+3*1] and feld[2+3*0] == feld[2+3*2] and feld[2+3*0] in ['X','O']:
        return True
    
    #waagrecht
    if feld[0+3*0] == feld[1+3*0] and feld[0+3*0] == feld[2+3*0] and feld[0+3*0] in ['X','O']:
        return True
    if feld[0+3*1] == feld[1+3*1] and feld[0+3*1] == feld[2+3*1] and feld[0+3*1] in ['X','O']:
        return True
    if feld[0+3*2] == feld[1+3*2] and feld[0+3*2] == feld[2+3*2] and feld[0+3*2] in ['X','O']:
        return True
    
    #diagonal
    if feld[0+3*0] == feld[1+3*1] and feld[0+3*0] == feld[2+3*2] and feld[0+3*0] in ['X','O']:
        return True
    if feld[0+3*2] == feld[2+3*0] and feld[0+3*2] == feld[1+3*1] and feld[1+3*1] in ['X','O']:
        return True
    
    #nix davon
    return False
    
if __name__ == '__main__':
    fertig = False
    zug = ''
    spieler = 'X'
    spielfeld = []
    spielfeld = spielanfang()
    
    while(fertig == False):

        print_grid(spielfeld)
        
        x = y = -1
        while(x not in [0,1,2] or y not in [0,1,2]):
            zug = input('Zeile + Spalte (z.B. 00 für oben links):')
        
            x = int(zug[1])
            y = int(zug[0])
        
        if spielfeld[x+3*y]== '.':
            spielfeld[x+3*y] = spieler
            
            fertig = istFertig(spielfeld)
            if spieler == 'X':
                spieler = 'O'
            else:
                spieler = 'X'
        
    print_grid(spielfeld)
        