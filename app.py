import os
from converter import cambiar_formato_imagen
from flask import Flask, render_template, request, send_file              #flask es un "micro framework" para crear aplicaciones web, me va a ayudar a darle funcionalidad web a mi programa

app = Flask(__name__)                                                     #declaramos la inizializacion de flask

CARPETA_SUBIDAS = 'uploads'                                               #declaramos la carpeta donde se van a guardar las imagenes subidas
os.makedirs(CARPETA_SUBIDAS, exist_ok=True)                               #si la mista no existe la creamos

@app.route('/')                                                           #indica la ruta principal de la aplicacion
def inicio():                                                             #def_inicio(): es la funcion que se va a ejecutar cuando se acceda a la ruta principal
    return render_template('index.html')                                  #renderiza el archivo index.html

@app.route('/convertir', methods=['POST'])                                #indica la ruta para convertir la imagen, solo acepta el metodo POST
def procesar():                                                           #funcion que se va a ejecutar cuando se acceda a la ruta /convertir
    try:
        archivo = request.files['archivo_del_usuario']                    #obtenemos el archivo subido por el usuario
        formato = request.form['formato_a_cambiar']                       #obtenemos el formato al que el usuario quiere cambiar la imagen

        if archivo.filename == '':             
            return "No seleccionaste ningún archivo."                     #verificamos que el usuario haya subido un archivo     

        ruta_original = os.path.join(CARPETA_SUBIDAS, archivo.filename)   #creamos la ruta completa del archivo subido
        archivo.save(ruta_original)                                       #guardamos el archivo en la carpeta de uploads 

        ruta_convertida = cambiar_formato_imagen(ruta_original, formato)  #llamamos a la funcion cambiar_formato_imagen para convertir la imagen

        return send_file(ruta_convertida, as_attachment=True)             #enviamos el archivo convertido al usuario para que lo descargue

    except Exception as e:                                                #si no se cumple alguna de las condiciones anteriores, devolvemos un error
        return f"Ocurrió un error: {e}"

if __name__ == '__main__':                                                #si el archivo es ejecutado directamente, iniciamos la aplicacion web
    app.run(debug=True)