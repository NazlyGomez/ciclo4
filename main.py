import met as met
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
mesacontrolador = ControladorMesa()

from Controladores.ControladorPartido import ControladorPartido
partidoControlador = ControladorPartido()

from Controladores.ControladorPersona import ControladorPersona
personaControlador = ControladorPersona()

from Controladores.ControladorResultado import ControladorResultado
resultadoControlador = ControladorResultado()


"RUTAS METODOS CRUD "
@app.route("/Mesa", methods=['GET'])
def getMesa():
    json = mesacontrolador.index()
    return jsonify(json)


@app.route("/Mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = mesacontrolador.create(data)
    return jsonify(json)


@app.route("/Mesa/<string:id_Mesa>", methods=['GET'])
def getmesa(id_Mesa):
    json = mesacontrolador.show(id_Mesa)
    return jsonify(json)


@app.route("/Mesa/<string:id_Mesa>", methods=['PUT'])
def modificarMesa(id_Mesa):
    data = request.get_json()
    json = mesacontrolador.update(id_Mesa, data)
    return jsonify(json)


@app.route("/Mesa/<string:id_Mesa>", methods=['DELETE'])
def eliminarMesa(id_Mesa):
    json = mesacontrolador.delete(id_Mesa)
    return jsonify(json)


@app.route("/Partido", methods=['GET'])
def getPartido():
    json = partidoControlador.index()
    return jsonify(json)


@app.route("/Partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = partidoControlador.create(data)
    return jsonify(json)


@app.route("/Partido/<string:id_Partido>", methods=['GET'])
def getpartido(id_Partido):
    json = partidoControlador.show(id_Partido)
    return jsonify(json)


@app.route("/Partido/<string:id_Partido>", methods=['PUT'])
def modificarPartido(id_Partido):
    data = request.get_json()
    json = partidoControlador.update(id_Partido, data)
    return jsonify(json)


@app.route("/Partido/<string:id_Partido>", methods=['DELETE'])
def eliminarPartido(id_Partido):
    json = partidoControlador.delete(id_Partido)
    return jsonify(json)


@app.route("/Persona", methods=['GET'])
def getPersona():
    json = personaControlador.index()
    return jsonify(json)


@app.route("/Persona", methods=['POST'])
def crearPersona():
    data = request.get_json()
    json = personaControlador.create(data)
    return jsonify(json)


@app.route("/Persona/<string:id_Persona>", methods=['GET'])
def getpersona(id_Persona):
    json = personaControlador.show(id_Persona)
    return jsonify(json)


@app.route("/Persona/<string:id_Persona>", methods=['PUT'])
def modificarPersona(id_Persona):
    data = request.get_json()
    json = personaControlador.update(id_Persona, data)
    return jsonify(json)


@app.route("/Persona/<string:id_Persona>", methods=['DELETE'])
def eliminarPersona(id_Persona):
    json = personaControlador.delete(id_Persona)
    return jsonify(json)


@app.route("/Resultado", methods=['GET'])
def getResultado():
    json = resultadoControlador.index()
    return jsonify(json)


@app.route("/Resultado", methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = resultadoControlador.create(data)
    return jsonify(json)


@app.route("/Resultado/<string:id_Resultado>", methods=['GET'])
def getresultado(id_Resultado):
    json = resultadoControlador.show(id_Resultado)
    return jsonify(json)


@app.route("/Resultado/<string:id_Resultado>", methods=['PUT'])
def modificarResultado(id_Resultado):
    data = request.get_json()
    json = resultadoControlador.update(id_Resultado, data)
    return jsonify(json)


@app.route("/Resultado/<string:id_Resultado>", methods=['DELETE'])
def eliminarResultado(id_Resultado):
    json = resultadoControlador.delete(id_Resultado)
    return jsonify(json)

"RUTAS RELACIONES"
@app.route("/Persona/<string:id_Persona>/Partido/<string:id_Partido>",methods=['PUT'])
def asignarPersonaAPartido(id_Persona,id_Partido):
    json=personaControlador.asignarPartido(id_Persona,id_Partido)
    return jsonify(json)

@app.route("/Resultado", methods=['GET'])
def getResultado_r():
    json = resultadoControlador.index()
    return jsonify(json)

@app.route("/Resultado/<string:id_Resultado>", methods=['GET'])
def getresultado_r(id_Resultado):
    json = resultadoControlador.show(id_Resultado)
    return jsonify(json)

@app.route("/Resultado/Persona/<string:id_Persona>/Mesa/<string:id_Mesa>",methods=['POST'])
def CrearResultado(id_Persona,id_Mesa):
    data = request.get_json()
    json = resultadoControlador.create(data, id_Persona, id_Mesa)
    return jsonify(json)

@app.route("/Resultado/<string:id_Resultado>/Persona/<string:id_Persona>/Mesa/<string:id_Mesa>",methods=['PUT'])
def ModificarResultado(id_Resultado,id_Persona,id_Mesa):
    data = request.get_json()
    json = resultadoControlador.update(id_Resultado, data, id_Persona, id_Mesa)
    return jsonify(json)

@app.route("/Resultado/<string:id_Resultado>",methods=['DELETE'])
def eliminarInscripcion(id_Resultado):
    json=resultadoControlador.delete(id_Resultado)
    return jsonify(json)

"CONEXIONES"

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
