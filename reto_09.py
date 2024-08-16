# HERENCIA Y POLIMORFISMO

"""
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.

DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""

class Animal:
    def __init__(self):
        pass
    
    def sound(self):
        print("Este animal emite algún sonido.")

class Dog(Animal):
    def sound(self):
        print("El perro hace 'guau'.")

class Cat(Animal):
    def sound(self):
        print("El gato hace 'miau'.")

#inicialización de clase y subclases
my_animal = Animal()
my_animal.sound()
my_dog = Dog()
my_dog.sound()
my_cat = Cat()
my_cat.sound()

# DIFICULTAD EXTRA

#superclase
class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employee = []
    
    def add_employees(self, employee: str):
        self.employee.append(employee)
        print(f'Empleado añadido. Lista actualizada: {self.employee}')

#subclases con herencia múltiple
class Manager(Employee):
    def working(self):
        print(f'{self.name} coordina todos los proyectos de la empresa.')

class ProjectManager(Manager):
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project
    
    def working(self):
        print(f'{self.name} coordina el proyecto {self.project}.')

class Programmer(ProjectManager):
    def __init__(self, id: int, name: str, project: str, language: str):
        super().__init__(id, name, project)
        self.language = language
    
    def working(self):
        print(f'{self.name} programa en el proyecto {self.project} con el lenguaje {self.language}.')
    
    def add_employees(self, employee: str):
        print(f'Los programadores no tienen empleados a cargo. {employee} no fue añadido.')

my_manager = Manager(1, 'Juan')
my_manager.working()
my_manager.add_employees('Pedro')
my_manager.add_employees('Ana')

my_proj_manager = ProjectManager(2, 'Ana', 'Proj 1')
my_proj_manager.working()
my_proj_manager.add_employees('Julio')

my_programmer = Programmer(2, 'Julio', 'Proj 1', 'Python')
my_programmer.working()
my_programmer.add_employees('Juan')