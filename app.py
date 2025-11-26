import os
from flask import Flask, render_template, request, send_file
from converter import cambiar_formato_imagen

app = Flask(__name__)

CARPETA_SUBIDAS = 'uploads'
os.makedirs(CARPETA_SUBIDAS, exist_ok=True)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/convertir', methods=['POST'])
def procesar():
    try:
        archivo = request.files['archivo_usuario']
        formato = request.form['formato_destino']

        if archivo.filename == '':
            return "No seleccionaste ningún archivo."

        ruta_original = os.path.join(CARPETA_SUBIDAS, archivo.filename)
        archivo.save(ruta_original)

        ruta_convertida = cambiar_formato_imagen(ruta_original, formato)

        return send_file(ruta_convertida, as_attachment=True)

    except Exception as e:
        return f"Ocurrió un error: {e}"

if __name__ == '__main__':
    app.run(debug=True)