"""
    author: @Jorgeflowers18
    Ejercicio 2: Dadas las siguiente ciudades, filtrar aquellas 
    que tienen un número par como longitud en sus caracteres.

    Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  
    Portoviejo, Macas
"""

ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra" , "Manabi", "Machala", "Portoviejo", "Macas"]

def org (x):

    if len(x) % 2 == 0:
        return True
    else:
        return False

ans = filter(org, ciudades)
print(list(ans))