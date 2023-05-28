libros = {
'Libro1' : {'autor' : 'autor1', 'año' : 2000, 'paginas': 350},
'Libro2' : {'autor' : 'autor2', 'año' : 2005, 'paginas': 250},
'Libro3' : {'autor' : 'autor1', 'año' : 2010, 'paginas': 400},
'Libro4' : {'autor' : 'autor3', 'año' : 2015, 'paginas': 150}
}

def buscar_libros_por_autor (libros,autor):
    libros_del_autor =[]
    for libro, info in libros.items ():
        if info ['autor'] == autor:
           libros_del_autor.append (libro)
    return libros_del_autor 
    
autor_buscar = 'autor1'
resultados = buscar_libros_por_autor (libros, autor_buscar)
print (resultados)