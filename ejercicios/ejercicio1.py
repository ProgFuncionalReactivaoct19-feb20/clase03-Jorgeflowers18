"""
    author: @Jorgeflowers18
    Ejercicio 1: Dado un conjunto de palabras, filtrar todas aquellas que sean palíndromas.
"""

palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

ans = filter(lambda x: x == "".join(reversed(x)), palabras)


print(list(ans))