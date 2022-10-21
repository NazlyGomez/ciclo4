import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorPersona import ControladorPersona
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

Mesacontrolador = ControladorMesa()
PartidoControlador = ControladorPartido()
PersonaControlador = ControladorPersona()
ResultadoControlador = ControladorResultado()



@app.route("/Mesa", methods=['GET'])
def getMesa():
    json = Mesacontrolador.index()
    return jsonify(json)


@app.route("/Mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = Mesacontrolador.create(data)
    return jsonify(json)


@app.route("/Mesa/<int:Codigo>", methods=['GET'])
def getmesa(Codigo):
    json = Mesacontrolador.show(Codigo)
    return jsonify(json)


@app.route("/Mesa/<int:Codigo>", methods=['PUT'])
def modificarMesa(Codigo):
    data = request.get_json()
    json = Mesacontrolador.update(Codigo, data)
    return jsonify(json)


@app.route("/Mesa/<int:Codigo>", methods=['DELETE'])
def eliminarMesa(Codigo):
    json = Mesacontrolador.delete(Codigo)
    return jsonify(json)


@app.route("/Partido", methods=['GET'])
def getPartido():
    json = PartidoControlador.index()
    return jsonify(json)


@app.route("/Partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = PartidoControlador.create(data)
    return jsonify(json)


@app.route("/Partido/<int:Codigo>", methods=['GET'])
def getpartido(Codigo):
    json = PartidoControlador.show(Codigo)
    return jsonify(json)


@app.route("/Partido/<int:Codigo>", methods=['PUT'])
def modificarPartido(Codigo):
    data = request.get_json()
    json = PartidoControlador.update(Codigo, data)
    return jsonify(json)


@app.route("/Partido/<int:Codigo>", methods=['DELETE'])
def eliminarPartido(Codigo):
    json = PartidoControlador.delete(Codigo)
    return jsonify(json)


@app.route("/Persona", methods=['GET'])
def getPersona():
    json = PersonaControlador.index()
    return jsonify(json)


@app.route("/Persona", methods=['POST'])
def crearPersona():
    data = request.get_json()
    json = PersonaControlador.create(data)
    return jsonify(json)


@app.route("/Persona/<string:Cedula>", methods=['GET'])
def getpersona(Cedula):
    json = PersonaControlador.show(Cedula)
    return jsonify(json)


@app.route("/Persona/<string:Cedula>", methods=['PUT'])
def modificarPersona(Cedula):
    data = request.get_json()
    json = PersonaControlador.update(Cedula, data)
    return jsonify(json)


@app.route("/Persona/<string:Cedula>", methods=['DELETE'])
def eliminarPersona(Cedula):
    json = PersonaControlador.delete(Cedula)
    return jsonify(json)


@app.route("/Resultado", methods=['GET'])
def getResultado():
    json = ResultadoControlador.index()
    return jsonify(json)


@app.route("/Resultado", methods=['POST'])
def crearResultado():
    data = request.get_json()
    json = ResultadoControlador.create(data)
    return jsonify(json)


@app.route("/Resultado/<string:ID>", methods=['GET'])
def getresultado(ID):
    json = ResultadoControlador.show(ID)
    return jsonify(json)


@app.route("/Resultado/<string:ID>", methods=['PUT'])
def modificarResultado(ID):
    data = request.get_json()
    json = ResultadoControlador.update(ID, data)
    return jsonify(json)


@app.route("/Resultado/<string:ID>", methods=['DELETE'])
def eliminarResultado(ID):
    json = ResultadoControlador.delete(ID)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
