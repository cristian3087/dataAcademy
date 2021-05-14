def palidromo():
    pal=input('Ingrese una palabra: ')
    pal=pal.lower()
    if(pal==pal[::-1]):
        print('La palabra: '+ pal + ' es palindromo')
    else:
        print('La palabra: '+ pal + ' NO es palindromo')


if __name__ =='__main__':
    palidromo()
