def pedir_dato(texto, fn):
    print(texto)
    dato = input()
    if(fn(int(dato))):
        return dato
    else:
        print("ERROR")
        print(pedir_dato(texto, fn))

def prueba(n):
    return n < 10

print(pedir_dato("hoola ingresá un número menor a 10: ", prueba))