import csv

def escribir_juego(matriz, diccionario, nombre):
    #nombre del archivo
    nombre_del_archivo = nombre + ".csv"
    print(nombre_del_archivo)

    with open(nombre_del_archivo, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        for lista in matriz:
            # writing the fields
            csvwriter.writerows(lista)
        







print(escribir_juego([[],[],[]], {"casa": {"x_inicial": 0, "x_final": 3, "y_inicial": 0, "y_final": 0}}, "nombre-del-archivo"))