"""
    author: @Jorgeflowers18
    Ejercicio 2: Dada las siguientes placas, filtrar aquellas que 
    pertenecen a las provincias de :
    Loja, Pichincha, Esmeraldas, Azuay, Imbabura    
    Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
"""

placas = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100" , "mab-001", "iaj-002"]

def org (x):

    pertenencia = ["l", "p", "e", "a", "i"]

    if x[0] in pertenencia:
        return True
    else:
        return False

ans = filter(org, placas)
print(list(ans))