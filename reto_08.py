# CLASES

'''
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.
'''

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_user(self):
        print(f'Usuario: {self.username} / Password: {self.password}')

new_user = User('miusuario', 'micontraseña')
new_user.get_user()
new_user.password = 'cambiodecontraseña'
new_user.get_user()

# DIFICULTAD EXTRA

class Stack:
    def __init__(self):
        self.stack = []

    def añadir(self, el):
        self.stack.append(el)
        print(f'Se añadió {el} a la pila.')
    
    def eliminar(self):
        if len(self.stack) == 0:
            print('La pila está vacía.')
        else:
            print(f'Se eliminó {self.stack.pop()} de la pila.')
    
    def cant_de_el(self):
        return len(self.stack)
    
    def contenido(self):
        for item in reversed(self.stack):
            print(item)

nueva_pila = Stack()
nueva_pila.añadir(1)
nueva_pila.añadir(2)
nueva_pila.añadir(3)
nueva_pila.contenido()
nueva_pila.eliminar()
print(f'Cantidad de elementos en la pila: {nueva_pila.cant_de_el()}')
nueva_pila.contenido()

class Queue:
    def __init__(self):
        self.queue = []

    def añadir(self, el):
        self.queue.append(el)
        print(f'Se añadió {el} a la cola.')
    
    def eliminar(self):
        if len(self.queue) == 0:
            print('La cola está vacía.')
        else:
            print(f'Se eliminó {self.queue.pop(0)} de la cola.')
    
    def cant_de_el(self):
        return len(self.queue)
    
    def contenido(self):
        print(f'Elementos en la cola: {self.queue}')

nueva_cola = Queue()
nueva_cola.añadir('Pedro')
nueva_cola.añadir('José')
nueva_cola.añadir('Ana')
nueva_cola.contenido()
nueva_cola.eliminar()
print(f'Cantidad de elementos en la cola: {nueva_cola.cant_de_el()}')
nueva_cola.contenido()
nueva_cola.eliminar()
print(f'Cantidad de elementos en la cola: {nueva_cola.cant_de_el()}')
nueva_cola.contenido()