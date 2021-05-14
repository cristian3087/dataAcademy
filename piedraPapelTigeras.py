def menu():
    print('****MENU**** \n Piedra \n Papel \n tigera \n ')


def juego():
    menu()
    j1=input('Jugador 1. Ingresar opción: ').lower()
    j2=input('Jugador 2. Ingresar opción: ').lower()
    #print('\n'+'imprimir j1=' + j1 + " j2=" + j2 +'\n')
    if(j1==j2):
        print('Empate')
    elif(j1=='papel' and j2!="tijera"):
        print('Gano jugador 1 con',j1)
    
    elif(j1=='piedra' and j2!="papel"):
        print('Gano jugador 1 con',j1)
    elif(j1=='tijera' and j2!="piedra"):
        print('Gano jugador 1 con',j1)    
    else:    
        print('Gano jugador 2 con', j2)
 

if __name__=='__main__':
    juego()