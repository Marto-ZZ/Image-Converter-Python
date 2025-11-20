from PIL import Image  #Importamos la libreria Pillow para el manejo de imagenes
import os              #Importamos la libreria os para el manejo de archivos, directorios y extensiones

def convertir_imagen_a_jpg(directorio_imagen):  #funcion que toma una imagen y la convierte a formato .jpg
    imagen = Image.open(directorio_imagen)      #localizamos la direccion de la imagen en el sistema
    
    if imagen.mode in ("RGBA", "P"):                                #verifica que nuestra imagen tenga un canal alfa, osea transparencia
        imagen = imagen.convert("RGB")                              #eliminamos el canal alfa que es el que da la transparencia
    imagen_sin_extension, _ = os.path.splitext(directorio_imagen)   #creamos una variable con el nombre del archivo y sin su extension, os lo toma como una tupla asi que lo que importa es el primer componenete que es el nombre
    nombre_a_jpg = f"{imagen_sin_extension}.jpg"                    #creamos la variable a devolver con el nombre original anidado a un .jpg
    imagen.save(nombre_a_jpg, "JPEG")                               #guardamos la imagen como un archivo .jpg


def convertir_imagen_a_png(directorio_imagen):                  #funcion que toma una imagen y la convierte a formato .png
    imagen = Image.open(directorio_imagen)                      #localizamos la direccion

    imagen_sin_extension, _ = os.path.splitext(directorio_imagen)  #creamos una variable que contenga el nombre del archivo sin su extension
    nombre_a_png = f"{imagen_sin_extension}.png"                   #creamos la variable a devolver con el nombre original anidado a un .png
    imagen.save(nombre_a_png, "PNG")                               #el codigo guarda esta imagen en formato .png