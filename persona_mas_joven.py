
def persona_mas_joven ():
    numpersonas = int (input("ingrese numero de personas: "))
    personas = {}

    for t in range (numpersonas):
        nombre = input ("ingrese nombre: ")
        edad = int (input("ingrese edad: "))
        personas [nombre] = edad

    persona_mas_joven = min (personas, key = personas.get)
    return persona_mas_joven

joven = persona_mas_joven ()

print ("la persona mas joven es: ", joven)