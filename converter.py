from PIL import Image                                               #Importamos la libreria Pillow para el manejo de imagenes
import os                                                           #Importamos la libreria os para el manejo de archivos, directorios y extensiones

def cambiar_formato_imagen(directorio_imagen, formato_a_cambiar):   #funcion que toma una imagen y la convierte al formato que se le indique

    imagen = Image.open(directorio_imagen)                          #localizamos la direccion de la imagen en el sistema
    extension_final = formato_a_cambiar.strip(".").lower()          #obtenemos la extension en minusculas y sin puntos

    if extension_final in ["jpg", "jpeg"]:                          #si es jpg o jpeg verificamos que no tenga canal alfa (transparencia)
        if imagen.mode in ("RGBA", "P"):                            
            imagen = imagen.convert("RGB")

    nombre_archivo, _ = os.path.splitext(directorio_imagen)         #creamos una variable con el nombre del archivo sin su extension, os lo toma como una tupla asi que lo que importa es el primer componenete que es el nombre

    if extension_final == "jpeg":                                   #si la extension final es jpeg la cambiamos a jpg para evitar confusiones
        extension_archivo = "jpg"
    else:
        extension_archivo = extension_final

    nombre_final = f"{nombre_archivo}.{extension_archivo}"          #creamos la variable a devolver con el nombre original anidado a la nueva extension

    if extension_final in ["jpg", "jpeg"]:                          #pillow usa "JPEG" para ambos formatos
        formato_de_pillow = "JPEG"
    else:
        formato_de_pillow = extension_final.upper()                 #si no es jpg o jpeg usamos la extension en mayusculas como formato de pillow

    imagen.save(nombre_final, format=formato_de_pillow)             #guardamos la imagen en el nuevo formato