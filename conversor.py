# 1 milla = 1.609344 km
def menu():
    print('****MENU**** ')
    print('1. Conversor de KM a Milla')
    print('2. Conversor de Mila a Km')
    print('3. Salir\n')


def convertir():
    menu()
    op=8
    km=1.609344
    while op!=3:
        op=int(input('Escoja la conversion: '))
       
        if(op==1):
            n=float(input('Ingrese los KM:'))
            print(str(n) +' km  son: '+str((n/km)) +' Millas'  )
        if(op==2):
            n=float(input('Ingrese los Millas:'))
            print(str(n) +' km  son: '+ str(n*km) +' Millas'  )

        print('op=',op)
    


if __name__=='__main__':
   convertir()