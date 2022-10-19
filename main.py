from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Ciclo4.Controladores.ControladorEstudiante import ControladorEstudiante
app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()
from Controladores.ControladorDepartamento import ControladorDepartamento
miControladorDepartamento=ControladorDepartamento()

@app.route("/Departamentos",methods=['GET'])
def getDepartamento():
    json=miControladorDepartamento.index()
    return jsonify(json)
@app.route("/Departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    return jsonify(json)
@app.route("/Departamentos/<string:id>",methods=['GET'])
def getdepartamento(id):
    json=miControladorDepartamento.show(id)
    return jsonify(json)
@app.route("/Departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    return jsonify(json)
@app.route("/Departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
    return jsonify(json)
@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    return jsonify(json)
@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    return jsonify(json)

@app.route("/primertest/<string:Nombre>", methods=['GET'])
def testmetodoget(Nombre):
    Variablerespuestaget = {
        "Esta es la respuesta del get": "...",
        "Nombre":Nombre
    }
    return Variablerespuestaget
@app.route("/primertest", methods=['POST'])
def testmetodopost():
    Variablerespuestapost = {
        "............": "..."
    }
    return Variablerespuestapost

@app.route("/primertest", methods=['PUT'])
def testmetodoput():
    Variablerespuestaput = {
        "Esta es la respuesta del put": "..."
    }
    return Variablerespuestaput

@app.route("/primertest", methods=['DELETE'])
def testmetododelete():
    Variablerespuestadelete = {
        "Esta es la respuesta del delete": "..."
    }
    return Variablerespuestadelete

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])





