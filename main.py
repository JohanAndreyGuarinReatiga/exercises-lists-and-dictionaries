from menu.exerciseOne import designOneList, designOneDict

while True:
    options = input(""" 
        Ejercicios de Listas y Tuplas
            1. Ejercicio 1
        Ejercicios de Diccionarios
            2. Ejercicio 1
""")
    match options:
        case 1:
            designOneList()
        case 2:
            designOneDict
        case _:
            print("Enter a valid option")
            
    #designOneDict()
