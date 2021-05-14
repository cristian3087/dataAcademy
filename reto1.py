#Reto 1- Area de un triangulo
#A = (b * h) / 2 
def tipoTriangulo():
    a=input('Ingrese el valor del lado a:')
    b=input('Ingrese el valor del lado b:')
    c=input('Ingrese el valor del lado c:')
    
    if(a==b and b==c):
        print('triángulo Equilatero')
    elif(a!=b and b!=c and a!=c):
         print('triángulo Escaleno')
    else:
        print('triángulo Isósceles')

def areaTriangulo():
    base=float(input('Ingrese la base del triángulo: '))
    altura=float(input('Ingrese la altura de un triángulo: '))
    area=(base*altura)/2
    print('El área del triángulo es: ',area)
    
if __name__=='__main__':
    areaTriangulo()
    tipoTriangulo()