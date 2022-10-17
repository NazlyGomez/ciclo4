from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorEstudiante import ControladorEstudiante

app=Flask(__name__)
cors = CORS(app)

controladorEstudiante = ControladorEstudiante()

@app.route("/estudiante",methods=['POST'])
def crearestudiante():
    requestBody = request.get_json()
    print("Este es el objeto que recibo en python ", requestBody)
    resultado = controladorEstudiante.create(requestBody)
    if resultado:
        return{"resultado": "Estudiante creado con exito"}
    else:
        return {"resultado": "Error al crear el estudiante"}
    return{"Resultado" : "EstudianteCreado"}

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=controladorEstudiante.index()
    return jsonify(json)
@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=controladorEstudiante.create(data)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=controladorEstudiante.show(id)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=controladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=controladorEstudiante.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

