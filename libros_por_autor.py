#esta actividad estaba resuelta en los apuntes pero quise agregarle que pueda ser buscado por un usuario.

def buscar_libros_por_autor(autor, libros):
    resultados = []
    for libro, autor_libro in libros.items():
        if autor_libro == autor:
            resultados.append(libro)
    return resultados

# Diccionario de libros con sus autores
libros = {
    "titulo: 'Nada' \naño: 1994 \npaginas: 336": "Carmen Laforet",
    "titulo: 'Cronicas Marcianas' \naño: 1950 \npaginas: 263": "Ray Bradbury",
    "titulo: 'Las Voces' \naño: 1957 \npaginas: 264": "Muriel Spark",
    "titulo: 'El Señor de las Moscas' \naño: 1954 \npaginas: 288": "William Golding",
    "titulo: 'Infinito en un Junco' \naño: 2019 \npaginas: 452": "Irene Vallejo",
    "titulo: 'Farenheit 451' \naño: 1953 \npaginas: 224": "Ray Bradbury",
    "titulo: 'El Hombre Ilustrado' \naño: 1951 \npaginas: 320": "Ray Bradbury",
    "titulo: 'Memento Mori' \naño: 1959 \npaginas: 276": "Muriel Spark",
    "titulo: 'La Oscuridad Visible' \naño: 1979 \npaginas: 329": "William Golding",
    "titulo: 'El Silbido del Arquero' \naño: 2015 \npaginas: 210": "Irene Vallejo",
}

autor_buscar = input("Ingresa el nombre del autor: ")
print ("\n")

resultados = buscar_libros_por_autor(autor_buscar, libros)

if resultados:
    print("Libros encontrados del autor", autor_buscar + ":", "\n")
    for libro in resultados:
        print(libro, "\n")
else:
    print("No se encontraron libros del autor", autor_buscar)
