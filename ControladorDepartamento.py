from Ciclo4.Modelos.Departamento import Departamento


class ControladorDepartamento():
    def __init__(self):
        print("Creando ControladorDepartamento")
    def index(self):
        print("Listar todos los departamentos")
        unDepartamento = {
            "Departamento": "Salud",
            "Codigo": "abc123",
            "Carreras": "24",
        }
        return [unDepartamento]
    def create(self,infoDepartamento):
        print("Crear un departamento")
        elDeparamento = Departamento (infoDepartamento)
        return elDeparamento.__dict__
    def show(self, id):
        print("Mostrando un Departamento con id ", id)
        elDepartamento = {
            "_id": "abc123",
            "Departamento": "Ingenieria"
        }
        return [elDepartamento]

    def update(self, id, infoDepartamento):
        print("Actualizando Departamento con id ", id)
        elDepartamento = Departamento(infoDepartamento)
        return elDepartamento.__dict__
    def delete(self, id):
        print("Eliminando departamento con id ", id)
        return {"deleted_count": 1}
