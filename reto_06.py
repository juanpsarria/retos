# RECURSIVIDAD

'''
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.

DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
sucesión de Fibonacci (la función recibe la posición).
'''

def recursividad(n):
    '''Función que devuelve el número ingresado y va disminuyendo hasta llegar al cero.

    Args:
        n (int): El argumento debe ser un número positivo.
    '''
    if n == 0:
        print(n)
    else:
        print(n)
        recursividad(n-1)

#se ejecuta la función de recursividad
recursividad(100)

# DIFICULTAD EXTRA

def factorial(n):
    '''Función que calcula el factorial del argumento.

    Args:
        n (int): El argumento debe ser >= 1.

    Returns:
        int: Retorna el factorial del número ingresado como argumento.
    '''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

def fibonacci(n):
    '''Fibonacci es una serie de números en la que cada número es la suma 
    de los dos números anteriores. 

    Args:
        n (int): El argumento debe ser mayor o igual a 0, indica la posición de la sucesión de Fibonacci que se quiere calcular.

    Returns:
        int: Retorna el valor al que corresponde la posición pasada como argumento.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))