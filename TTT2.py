

def print_grid(status):
    print(status)
    for i in [0,3,6]:
            print(status[i],'|',status[i+1],'|',status[i+2])
            
def spielanfang():
    status = []
    for i in range(0,9):
        status.append('.')
    return status

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
        
            x = int(zug[0])
            y = int(zug[1])
        
        if spielfeld[x+3*y]== '.':
            spielfeld[x+3*y] = spieler

            if spieler == 'X':
                spieler = 'O'
            else:
                spieler = 'X'
        
        