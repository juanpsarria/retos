# VALOR Y REFERENCIA

'''
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como
variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime
el valor de las variables originales y las nuevas, comprobando que se ha invertido
su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
'''

a = 1
b = 2
print(a, b)
b = a
print(a, b)

# copia por referencia, los cambios afectan a ambas listas
a = [1, 2, 3]
b = a
b.remove(2)
print(a, b)
print(id(a), id(b))

# copia por valor, los cambios afectan a la que se le realizan las operaciones
a = [1, 2, 3]
b = list(a)
b.remove(2)
print(a, b)
print(id(a), id(b))

# lo mismo sucede con los diccionarios
a = {1:'A', 2:'B', 3:'C'}
b = a
b.pop(2)
print(a, b)

a = {1:'A', 2:'B', 3:'C'}
b = dict(a)
b.pop(2)
print(a, b)

a = (1, 2, 3)
b = a

# función con paso con valor (se crea una copia local de la variable dentro de la función)
def doblar_valor(numero):
    numero *= 2
#la variable debe contener un tipo de dato simple (int, float, str, bool)
n = 10
doblar_valor(n)
print(n)

#función con paso con referencia (se maneja directamente la variable, los cambios realizados dentro de la función le afectarán también fuera.)
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
#se deben pasar tipos de datos compuestos (list, dict, set)
ns = [10,50,100]
doblar_valores(ns)
print(ns)
#para evitar la modificación: doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]

#DIFICULTAD EXTRA

def intercambiar_variables(a, b):
    '''Función que intercambia el valor de los parámetros entre sí.

    Args: Requiere dos argumentos: a, b
        a (int, float, str, bool)
        b (int, float, str, bool)

    Returns:
        El valor de a se asigna a b y viceversa.
    '''
    a, b = b, a
    return a, b

a = 10
b = 5
c,d = intercambiar_variables(a, b)

print('El valor original de las variables es',a, b)
print('El valor invertido es',c, d)

e = [1, 2, 3]
f = [4, 5, 6]
g,h = intercambiar_variables(e, f)
print('El valor original de las variables es',e, f)
print('El valor invertido es',g, h)
