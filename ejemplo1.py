"""
    Ejemplo 1: manejo de Funciones de orden superior
    author: @Jorgeflowers18
"""

def suma(a, b):
    return a + b

def producto (a, b):
    return a * b

def disparador(f, a ,b):
    print(f(a, b))

disparador(producto, 1, 10)
disparador(suma, 1 , 10)