import random

def generar_tablero(n, listaPalabras):
    contador = 0 #Sirve para el while
    tablero = [] #Tablero
    contadorRandom = "" #Sirve para el random, es un string con números
    while(contador < n):
        tablero.append([]) #creo tablero con listas
        contadorRandom = contadorRandom + str(contador) #String de numeros
        contador += 1 #Contador
    #Lleno el tablero de espacios, puedo usar ésta función para llenar de letras aleatorias despues
    for array in tablero:
        for item in range(0, n):
            array.append(" ")
    # print("tablero: ")
    print("contador random " + contadorRandom)

    def generarUbicacionAleatoriaHorizontal(y, x_inicial, pal):
        ubicacion = {
            "x_inicial": x_inicial,
            "x_final": int(x_inicial) + len(pal)-1,
            "y_inicialfinal" : y
        }
        return ubicacion

    def buscarEnElCursor(x,y):
        if(tablero[y][x] == " "):
            return True
        else:
            return False

    def insertarPalabraHorizontal(pal, x_inicial, y):
        cursor = x_inicial
        cursorPalabra = 0
        while(cursorPalabra < len(pal)):
            if(buscarEnElCursor(cursor, y)):
                tablero[y][cursor] = pal[cursorPalabra]
                cursor += 1
        if(cursor == len(pal)):
            return True
        else:
            return False

    def generarUbicacionAleatoriaVertical(y_inicial, x, pal):
        ubicacion = {
            "y_inicial": y_inicial,
            "y_final": int(y_inicial) + len(pal)-1,
            "x_inicialfinal" : x
        }
        return ubicacion

    def insertarPalabraVertical(pal, y_inicial, x):
        cursor = y_inicial
        for letra in pal:
            if(buscarEnElCursor(cursor, x)):
                tablero[x][cursor] = letra
                cursor += 1
        if(cursor == len(pal)):
            return True
        else:
            return False

    def generarTableroEnBlanco():
        tablero = []
        contador = 0 
        while(contador < n):
            tablero.append([])
            contador += 1
        for array in tablero:
            for item in range(0, n):
                array.append(" ")
        

    #meto palabras en tablero
    for palabra in listaPalabras:
        microContadorRandom = "" #string de numeros para el random, 
        microContador = 0
        ub = n-len(palabra)
        while(microContador<=ub):
            microContadorRandom = microContadorRandom + str(microContador) #llenamos el micro contador para el random, string con numeros
            microContador += 1
        
        # if(random.choice("a") == "a"): #Horizontal
        if(True):
            print("horizontal")
            cargaExitosa = False
            while(cargaExitosa == False):
                #Genero ubicación aleatoria
                ubicacion = generarUbicacionAleatoriaHorizontal(random.choice(contadorRandom), random.choice(microContadorRandom), palabra)
                # print("Ubicación: ")
                # print(ubicacion)
                #inserto palabra
                if(insertarPalabraHorizontal(palabra, int(ubicacion["x_inicial"]), int(ubicacion["y_inicialfinal"])) == False):
                    generarTableroEnBlanco()
                else:
                    cargaExitosa = True

        else: #vertical
            print("vertical")
            cargaExitosa = False
            while(cargaExitosa == False):
                #Genero ubicación aleatoria
                ubicacion = generarUbicacionAleatoriaVertical(random.choice(microContadorRandom), random.choice(contadorRandom), palabra)
                # print("Ubicación: ")
                # print(ubicacion)
                #inserto palabra
                if(insertarPalabraVertical(palabra, int(ubicacion["y_inicial"]), int(ubicacion["x_inicialfinal"])) == False):
                    generarTableroEnBlanco()
                else:
                    cargaExitosa = True

    for lista in tablero:
        print(*lista, sep="|")




lista = ["ola", "pi"]
print(generar_tablero(6, lista))