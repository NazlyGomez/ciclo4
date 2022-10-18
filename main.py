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
def crearEstudiante():
    requestBody = request.get_json()
    print("Este es el objeto que recibo en python ", requestBody)
    resultado = controladorEstudiante.create(requestBody)
    if resultado:
        return{"resultado": "Estudiante creado con exito"}
    else:
        return {"resultado": "Error al crear el estudiante"}
    return{"Resultado" : "EstudianteCreado"}

@app.route("/TEST-947/<string:Cedula>",methods=['GET'])
def test(Cedula):
    json = {}
    json2={}
    json["message"]="juan sebastian ...",
    json2["Cedula"] = Cedula
    return jsonify(json,json2)

@app.route("/TEST-947",methods=['PUT'])
def test2():
    json = {}
    json["message"]="sebastian ..."
    return jsonify(json)

@app.route("/TEST-947",methods=['DELETE'])
def test3():
    json = {}
    json["message"]="juan  ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])