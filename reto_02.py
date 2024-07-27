#FUNCIONES Y ALCANCE

'''
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
    - Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    - Comprueba si puedes crear funciones dentro de funciones.
    - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    - Pon a prueba el concepto de variable LOCAL y GLOBAL.
    - Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

def bienvenida(): #sin parámetro ni retorno
    print('Bienvenida/o.')

def saludo(nombre): #con un parámetro, sin retorno
    print('Hola,', nombre)
    bienvenida() #función invocada dentro de otra función

saludo('Juan')

a = 8
b = 2

def suma(*args): #varios parámetros, con retorno
    return sum(args)

print(suma(10, 5, 5))
print(suma(a, b))

#DIFICULTAD EXTRA

def dos_param(a : str, b : str):
    vuelta = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, a + b)
        elif i % 5 == 0:
            print(i, b)
        elif i % 3 == 0 :
            print(i, a)
        else:
            vuelta += 1
            print(i, 'Número de veces que se ha impreso el número en lugar de los textos:', vuelta)

dos_param('Hola', 'Chau')