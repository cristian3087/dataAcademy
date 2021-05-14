def ingreseNumeros():
    li=int(input('Ingrese un # limite inferior: '))
    ls=int(input('Ingrese un # limite superior: '))
    b=True
    while(b!=False):
        n=int(input('Ingrese un # comparador: '))
        if(n>li and n<ls):
            print("\n El " +str(n) + ' esta en el rango entre '+ str(li)+'-'+str(ls)+'\n')
            b=False
        else:
            print('Fuera de rango')

if __name__=='__main__':
    ingreseNumeros()