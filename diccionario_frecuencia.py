cadenaPalabras = 'it was the best of times it was the worst of times '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Diccionario\n" + str(dict(zip(listaPalabras, frecuenciaPalab))))