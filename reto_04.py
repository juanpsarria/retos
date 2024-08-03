# CADENAS DE CARACTERES

'''
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
'''

a = 'hola'
b = 'Python'
c = a + b

#Acceso a elementos de una cadena
print(a[1]) #imprime al elemento que se encuentra en la posición 1 de la variable a
print(b[1:4]) #imprime la subcadena que se forma entre los elementos de posición 1 y 3
print(b[2:]) #desde el elemento de posición 2 en adelante
print(b[:-2]) #número negativo inicia desde el final de la palabra

#Operaciones
print('+ Concatenación de cadenas: ', a+b)
print('* Repetición de una cadena: ', a*3)
print('in devuelve True o False:', a in b)
print('not in devuelve True o False:', a not in b)

#Comparación de cadenas
print('== o != comparan si una cadena es igual o diferente a otra, pueden devolver True o False: ', a == b) #ascii
print('> o < indican si una cadena sucede o antecede a otra: ', a > b)
print('>= o <= indican si una cadena sucede o es igual, o antecede o es igual a otra:', a <= b)

#Funciones con cadenas
print('len() devuelve el número de caracteres de la cadena:', len(a))
print('min() devuelve el carácter menor de la cadena:', min(b))
print('max() devuelve el carácter mayor de la cadena:', max(b))
print('.upper() devuelve la cadena con los mismos caracteres en mayúsculas', a.upper())
print('.lower() devuelve la cadena con los mismos caracteres en minúsculas', a.lower())
print('.title() devuelve la cadena con el primer carácter en mayúsculas y el resto en minúsculas:', a.title())
print('.split(delimitador) devuelve la lista formada por las subcadenas que resultan de partir la cadena usando como delimitador la cadena delimitador. Si no hay el delimitador, utiliza por defecto el espacio en blanco.', c.split('P'))
print('.find()  indica el índice de inicio del argumento:', a.find('l'), b.find('thon'))
print('.replace() cambia una sub-cadena de una cadena:', a.replace('h', 'H'))

#Cadenas formateadas
print('{}, {}. Soy {}. {despedida}'.format(a.title(), b, 'Juan', despedida = 'Chau.'))

#DIFICULTAD EXTRA

def palindrome(a, b):
    '''Función que valida si dos argumentos son políndromos o no. Sin return.

    Args:
        a (str): puede o no ser polídromo del argumento b.
        b (str): puede o no ser polídromo del argumento a.
    '''
    if a == b[::-1]:
        print('{} y {} son polídromos.'.format(a,b))
    else:
        print('{} y {} no son polídromos.'.format(a,b))

def anagram(a, b):
    '''Función que valida si dos argumentos son anagramas o no. Sin return.

    Args:
        a (str): puede o no ser anagrama del argumento b.
        b (str): puede o no ser anagrama del argumento a.
    '''
    if sorted(a) == sorted(b):
        print('{} y {} son anagramas.'.format(a,b))
    else:
        print('{} y {} no son anagramas.'.format(a,b))

def isogram(a):
    '''Función que determina si una palabra es un isograma. Sin return.

    Args:
        a (str): ingresar cualquier palabra.
    '''
    if len(a) == len(set(a)):
        print('{} es un isograma.'.format(a))
    else:
        print('{} no es un isograma.'.format(a))

