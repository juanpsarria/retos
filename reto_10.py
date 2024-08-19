# EXCEPCIONES

"""
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.
"""

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        return(f"Error: {e}.")
    except TypeError as e:
        return(f"Error: {e}.")
    else:
        return result

print(division(10, 2))
print(division(10, 0))
print(division(10, "A"))


lst = [1, 2, 3]

try:
    print(lst[3])
except IndexError as e:
    print(f"Error: {e}.")


# DIFICULTAD EXTRA

lst = [1, 0, 3, 4, 5]

def params(lst : list):
    if len(lst) < 4:
        raise IndexError
    elif lst[1] == 0:
        raise ZeroDivisionError
    elif lst[2] < 0:
        raise ValueError
    
    print(lst[4])
    print(lst[0]/lst[1])
    print(lst[2] + 5)

try:
    params(lst)
except IndexError as e:
    print("La lista debe ser mayor que 4")
except ZeroDivisionError as e:
    print("No se puede dividir por cero.")
except ValueError as e:
    print("El número debe ser mayor a 0.")
except Exception:
    print("Error inesperado.")
else:
    print("No se produjo ningún error")
finally:
    print("La ejecución ha finalizado.")
