def pedir_datos_tablero():
    #cantidad de columnas y filas
    print("Ingresá un número para establacer la cantidad de columnas y filas: ")
    N = int(input())
    #Validación

    #lista de palabras
    lista = []
    palabras_posibles = int(N/3)
    print("Ahora ingresá las palabras- Podés ingresar hasta " + str(palabras_posibles) + " palabras.")
    print("Y recordá que la longitud de la palabra tiene que ser menor a " + str(palabras_posibles) + ".")
    print("Para finalizar la carga escribí fin")
    palabra = ""
    while(len(lista) < palabras_posibles and palabra != "fin"):
        print("Ingresá una palabra: ")
        palabra = input()
        lista.append(palabra)
    #validación ??


    #nombre del archivo
    print("Ahora ingresá el nombre del archivo. Tiene que tener un máximo de 30 caracteres:")
    nombre = input()
    #validación

    return (N, lista, nombre)


print(pedir_datos_tablero())

