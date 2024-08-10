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
    '''
    Ingresar primero una de las páginas existentes en la lista paginas para ubicarse. Luego se
    puede ingresar otro elemento de la lista, adelante y atrás para moverse entre ellos, y fin para
    terminar el bucle while.
    Si se ingresa otro valor, se va a agregar a la lista paginas.
    '''
    navegar = input(f'Ingrese primero para navegar: {paginas}, o el nombre de la nueva web. Luego, para moverse puede utilizar los nombres de las páginas o los comandos adelante o atrás. Fin para salir. ').lower()
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
        actual = 0
        print(f'Has llegado al final de la lista. Estás en: {paginas[actual]}.')
    finally:
        navegar


documentos = ['doc1', 'doc2', 'doc3']

while documentos:
    ingreso = input('Ingrese el nombre del nuevo documento o imprimir, si así lo desea.').lower()
    
    if ingreso == 'imprimir':
        print(f'Imprimiendo documento: {documentos.pop(0)}')
        print(documentos)
    else:
        documentos.append(ingreso)
        print(f'Nuevo documento agregado a la cola: {documentos}.')
else:
    print('La cola de documentos se ha vaciado.')