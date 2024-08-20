# FICHEROS

"""
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.

DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
[nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""
#se importa os para poder eliminar el archivo
import os

#se crea el archivo y se le pasa texto
with open('juanpsarria.txt', 'w', encoding='utf-8') as file:
    file.write("Mi nombre es Juan.\n")
    file.write("Tengo 37 años.\n")
    file.write("Mi lenguaje de programación favorito es Python.")

#se lee el archivo y se imprime el contenido
with open('juanpsarria.txt', encoding='utf-8') as file:
    text = file.read()
    print(text)

#se elimina el archivo
os.remove('juanpsarria.txt')


# DIFICULTAD EXTRA

class SalesManagement:
    def __init__(self):
        with open('sales.txt', "w", encoding="utf-8"):
            pass
    
    def add_product(self):
        product_name = input("Ingrese el nombre del producto.").capitalize()
        quantity = int(input("Ingrese la cantidad."))
        price = float(input("Ingrese el precio."))
        with open('sales.txt', 'a', encoding="utf-8") as text:
            text.write(f"{product_name}, {quantity}, {price:.2f}")


my_sales = SalesManagement()
my_sales.add_product()