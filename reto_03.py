#ESTRUCTURAS DE DATOS

'''
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos 
(o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
'''

#Listas
lista = [1, 2, 3, ['cuatro', 'cinco']]
constructor_lista = list(("apple", "banana", "cherry"))
print(lista)
lista.append(6) #inserción al final
lista.insert(0, True) #inserción con especificación de índice
print(lista)
lista.remove(6) #borrado elemento indicado
lista.pop(0) #borra por índice
print(lista)
#lista.sort() #orden, siempre y cuando lo elementos sean comparables


#Tuplas
tupla = (1, 2, 3, ['cuatro', 'cinco'])
const_tupla = tuple(("apple", "banana", "cherry"))
print(tupla)
print(tupla.index(3)) #muestra el índice del elemento

#Diccionarios
diccionario = {'nombre' : 'Juan', 'teléfono': 123456, 'país' : 'Argentina'}
const_dicccionario = dict(name = "John", age = 36, country = "Norway")
print(diccionario)
diccionario.update({'apellido' : 'Sarria'}) #inserción o actualización
print(diccionario)
print(diccionario.pop('apellido')) #devuelve el valor y lo elimina
print(diccionario.popitem()) #devuelve tupla con el último par del diccionario y lo elimina
del diccionario['teléfono'] #borra el par indicado por la key
print(diccionario)
diccionario.clear() #vacía el diccionario
print(diccionario)

#Sets
sets = {1, 2, 3, 'cuatro', 'cinco'}
constructor_set = set((1, 2, 3, 'cuatro', 'cinco'))
print(sets)
sets.add(True) #inserción
print(sets)
lista = [4, 5, 6]
sets.update(lista) #agrega lista al set, sin repetir los elementos
print(sets)
sets.remove(1) #eliminar, si no existe da error
sets.discard(2) #eliminar, si no existe no da error
sets.pop() #elimina elemento al azar
print(sets)

#DIFICULTAD EXTRA

contact_list = {'Juan' : 3416635588 , 'Gabriel': 3413001516}

def create_contact():
    '''Función que crea un nuevo contacto.
    Requiere el ingreso de un nombre y un teléfono con 11 dígitos.
    Resultado: crea el nuevo contacto y lo ingresa en la agenda.
    '''
    name = input("Ingrese el nombre del contacto.")
    phone = int(input("Ingrese el número de teléfono del contacto (11 dígitos)."))
    while len(str(phone)) != 11:
        phone = input("Ingrese el número de teléfono del contacto (11 dígitos).")
    else:
        contact_list.update({name : phone})
        print('Contacto agendado exitosamente.')
        print(contact_list)

def read_contact():
    '''Función que busca un contacto en la agenda.
    Requiere el ingreso de un nombre.
    Resultado: muestra el número de teléfono del contacto buscado, si existe.
    '''
    name = input("Ingrese el nombre del contacto a buscar.")
    if name in contact_list:
        print(f"El número de teléfono de {name} es: {contact_list[name]}")
    else:
        print("El contacto no está en la agenda.")

def update_contact():
    '''Función que actualiza el número de teléfono de un contacto dado.
    Requiere el ingreso del contacto y luego su nuevo número de teléfono, de 11 digitos.
    Resultado: devuelve la lista con el contacto actualizado.
    '''
    name = input("Ingrese el nombre del contacto a actualizar.")
    if name in contact_list:
        phone = int(input("Ingrese el nuevo número de teléfono (11 dígitos)."))
        while len(str(phone)) != 11:
            phone = int(input("Ingrese el nuevo número de teléfono (11 dígitos)."))
        else:
            contact_list[name] = phone
            print('Contacto actualizado exitosamente.')
            print(contact_list)
    else:
        print("El contacto no está en la agenda.")

def delete_contact():
    '''Función que elimina un contacto seleccionado.
    Requiere el ingreso del nombre del contacto a eliminar.
    Resultado: devuelve la lista, en la cual ya no está el contacto eliminado.
    '''
    name = input("Ingrese el nombre del contacto a eliminar.")
    if name in contact_list:
        del contact_list[name]
        print('Contacto eliminado exitosamente.')
        print(contact_list)
    else:
        print("El contacto no está en la agenda.")

interaction = input('Ingrese A para actualizar contacto, B para buscarlo, C para crear un contacto nuevo o D para eliminar un contacto existente.').upper()

if interaction == 'A':
    update_contact()
elif interaction == 'B':
    read_contact()
elif interaction == 'C':
    create_contact()
elif interaction == 'D':
    delete_contact()
else:
    print("La opción ingresada no es válida.")