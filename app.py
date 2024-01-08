"""Este código devuelve un html que muestra la lista de posiciones"""

from flask import Flask, request, render_template
app = Flask(__name__)
# app.config['MIME_TYPES'] = {'js': 'application/javascript'}

# lista de posiciones
ld_pos = [{'id': "camion 1", 'lat': 19.028353, 'lon': -98.188938}]


def limpiar_lista():
    """limpia la lista, para que solo contenga las posiciones más recientes"""
    global ld_pos
    ids_list = []
    clean_list = []

    for dicc in ld_pos:
        if not dicc['id'] in ids_list:  # si no tengo guardado tu id
            ids_list.append(dicc['id'])  # guardar tu id
            # guardar el diccionario, primera aparición del id -> pos más reciente
            clean_list.append(dicc)

    ld_pos = clean_list


@app.route('/')
def index():
    """Vista llamada index, ligada a la ruta raíz, """
    return render_template('vista_de_usuario.html')


# @app.route('/static/js/<filename>')
# def serve_js(filename):
#     return send_from_directory('static/js', filename, mimetype='application/javascript')


@app.route('/posiciones', methods=['POST', 'GET'])
def app1():
    "Aquí el esp32 envía las posiciones, JS pide la lista limpia"
    global ld_pos

    # render_template('index.html', lista=ld_pos)

    if request.method == 'POST':
        if len(ld_pos) < 25:
            data = request.get_json()
            ld_pos.insert(0, data)
            verificacion = f"recibí {data}"
            return (verificacion)
        else:
            limpiar_lista()
    else:
        limpiar_lista()
        return ld_pos


@app.route('/ruta33', methods=['POST', 'GET'])
def obtenerlista():
    if request.method == 'GET':
        return (ld_pos)
    else:
        return ("recibí correctamente")


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
