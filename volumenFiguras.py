def menu():
    print('****MENU**** ')
    print('1. Calcular volumen de un cilindro')
    print('2. Calcular volumen de un cubo')
    print('3. Calcular volumen de la esfera')
    print('4. Salir\n')


def calcularVolumen():
    menu()
    op=8
    PI=3.141592
    while op!=4:
        op=int(input('Seleccione una opción: '))
       
        if(op==1):
            r=float(input('Ingrese el radio:'))
            h=float(input('Ingrese la altura del cilindro:'))

            print('El volumen del cilindro es: '+str((PI*(r*r)*h)))
        if(op==2):
            a=float(input('Longitud de la cara del cubo:'))
            print('El volumen del cubo: '+str((a**3)))

        if(op==3):
            r=float(input('Valor del radio:'))
            v=(4/3)*PI*r**3
            print('El volumen del cubo: '+str(v))


if __name__=='__main__':
    calcularVolumen()
