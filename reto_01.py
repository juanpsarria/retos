#OPERADORES Y ESTRUCTURAS DE CONTROL

'''
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

a = 8
b = 5
x = True
y = False

#Operadores aritméticos
print('Suma:', a + b)
print('Resta:', a - b)
print('Multiplicación:', a * b)
print('División:', a / b)
print('División entera:', a // b)
print('Resto división entera:', a % b)
print('Potencia:', a ** b)

#Operadores lógicos o booleanos
print('x or y:', x or y) #Si x se evalúa falso, entonces devuelve y, si no devuelve x
print('x and y:', x and y) #Si x se evalúa falso, entonces devuelve x, si no devuelve y
print('not x:', not x) #Si x se evalúa falso, entonces devuelve True, si no devuelve False

#Operadores de comparación
print('a es mayor que b:', a > b)
print('a es menor que b:', a < b)
print('a es igual que b:', a == b)
print('a es igual o mayor que b:', a >= b)
print('a es igual o menor que b:', a <= b)
print('a es distinto de b:', a != b)

#Operadores de asignación
print('El operador de asignación es =')

#Operadores de asignación compuestos
a=7; b=2
x=a; x+=b;  print("x +=", x)  # 9
x=a; x-=b;  print("x -=", x)  # 5
x=a; x*=b;  print("x *=", x)  # 14
x=a; x/=b;  print("x /=", x)  # 3.5
x=a; x%=b;  print("x %=", x)  # 1
x=a; x//=b; print("x //=", x) # 3
x=a; x**=b; print("x **=", x) # 49
x=a; x&=b;  print("x &=", x)  # 2
x=a; x|=b;  print("x |=", x)  # 7
x=a; x^=b; print("x ^=", x)   # 5
x=a; x>>=b; print("x >>=", x) # 1
x=a; x<<=b; print("x <<=", x) # 28

#Operadores de identidad
lista = [1, 2, 3]
print('is:', a is lista)
print ('is not:', a is not b)

#Operadores de pertenencia
print('in:', a in lista)
print('not in:', a not in lista)

#Operadores a nivel de bits
x, y = 2, 7

print('x | y, or bit a bit de x e y', x | y)
print('x ^ y, or exclusivo bit a bit de x e y', x ^ y)
print('x & y, and bit a bit de x e y', x & y)
print('x << n, desplaza x n bits a la izquierda', x << 1)
print('x >> n, desplaza x n bits a la derecha', x >> 1)
print('~x, not x. Obtiene los bits de x invertidos', ~x)

#Estructuras de control condicionales if y while con manejo de excepciones
usos = 0

while usos < 2:
    try:
        primer_num = int(input('Ingrese un número entero.'))
        operacion = input('Selecciones: +, -, *, /, para sumar, restar, multiplicar o dividir.')
        segundo_num = int(input('Ingrese otro número entero.'))
        
        if operacion == '+':
            resultado = primer_num + segundo_num
            print(primer_num, operacion, segundo_num, '=', resultado)
        elif operacion == '-':
            resultado = primer_num - segundo_num
            print(primer_num, operacion, segundo_num, '=', resultado)
        elif operacion == '*':
            resultado = primer_num * segundo_num
            print(primer_num, operacion, segundo_num, '=', resultado)
        elif operacion == '/':
            try:
                resultado = primer_num / segundo_num
            except ZeroDivisionError:
                print('Error: No se puede dividir por 0.')
            else:
                print(primer_num, operacion, segundo_num, '=', resultado)
        else:
            print('Error: Operación no válida.')
    except ValueError:
        print('Error: Ingreso inválido. Ingrese un número entero.')
    else:
        usos += 1
else:
    print('Ya no se puede seguir usando.')

#Estructura de control iterativa con ciclo for
frutas = ['banana', 'manzana', 'naranja']
for fruta in frutas:
    print(fruta)


#DIFICULTAD EXTRA

for i in range(10, 55, 2):
    if i == 16 or i % 3 == 0:
        continue
    else:
        print(i, end=' ')