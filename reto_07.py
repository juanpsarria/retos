# PILAS Y COLAS

'''
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).

DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
'''


queue = []
#introducción de elementos
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
#recuperación de los primeros datos ingresados (queue - first in first out)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)

stack = []
#introducción de elementos
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
#recuperación de los últimos datos ingresados (stack - last in first out)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

# DIFICULTAD EXTRA

paginas = ['home', 'productos', 'servicios', 'historia', 'contacto']

while paginas:
    navegar = input(f'Ingrese para navegar: {paginas}, o el nombre de la nueva web. Si se quiere mover puede utilizar los comandos adelante o atrás. Fin para salir. ').lower()
    try:
        if navegar in paginas:
            print(f'Estás en: {navegar}')
            actual = paginas.index(navegar)
        else:
            if navegar == 'atrás':
                actual -= 1
                print(f'Te has movido a: {paginas[actual]}')
            elif navegar == 'adelante':
                actual += 1
                print(f'Te has movido a: {paginas[actual]}')
            elif navegar == 'fin':
                break
            else:
                paginas.append(navegar)
                actual = paginas.index(navegar)
                print(f'Estás en la nueva web: {navegar}')
    except IndexError:
        actual -= 1
        print(f'Has llegado al final de la lista. Estás en: {paginas[actual]}.')
    finally:
        navegar
