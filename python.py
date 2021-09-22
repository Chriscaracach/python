# #Funcion para generar letras random
# import random

# def textoRandom(texto):
#     resultado = ""
#     for letra in texto:
#         if(letra == " "):
#             resultado = resultado + " "
#         else:
#             resultado = resultado + random.choice("abcdefghijklmnopqrstuvwxyz")

#     return resultado

# print(textoRandom("Hola que tal"))




#print(random.choice("abcdefghijklmnopqrstuvwxyz"))

#Recursion
# def buscar(lista, n):
#     i = 0
#     for elemento in lista:
#         if(elemento == n):
#             return i
#             i += 1
#     return None

# print("buscar 1")
# print(buscar([1,4,3,2,5,4,4,4], 6))


# def buscar2(lista, n, i=0):
#     if lista[i] == n:
#         return i
#     return buscar2(lista, n, i+1)

# print("buscar2")
# print(buscar2([1,4,3,2,5,4,4,4], 6))

#Factorial


# def fibonacciNormal(n):

#     contador = 2
#     fib = 1
#     seq = [1,1]
#     punteroMenosDos = len(seq)-2
#     punteroMenosUno = len(seq)-1
#     while(contador<n):
#         seq.append(punteroMenosDos + punteroMenosUno)
#         contador +=1
#     return seq[punteroMenosUno]


# print(fibonacciNormal(5))


