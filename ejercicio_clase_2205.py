# hice un codigo diferente al de la clase, no hice una funcion solo agregué detalles para que muestre mas cosas en pantalla,
# utilicé la funcion "split" que actua sobre una cadena y devuelve un alista de subcadenas, no utilicé un contador, a la 
# variable "listaPalabras" le agregué ".count(w)" para que agregue las repeticiones, convertí las lista en diccionario en el print
# y utilicé la funcion "zip", que es un iterador de tuplas donde el primer elemento de cada iterador pasado, se empareja y asi 
# sucesivamente 'las empareja'

print ("ingrese su oración:")
oracion= input ()

ingreso = oracion

listaPalabras = ingreso.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + ingreso +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Diccionario\n" + str(dict(zip(listaPalabras, frecuenciaPalab))))