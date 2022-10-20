from Modelos.Estudiante import Estudiante
from Repositorios.EstudianteRepositorio import EstudianteRepositorio


class ControladorEstudiante():
    def __init__(self):
        print("Creando ControladorEstudiante")
        self.estudianteRepositorio = EstudianteRepositorio()

    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unEstudiante]
    def create(self, infoEstudiante):
        print("Crear un estudiante")
        elEstudiante = Estudiante(infoEstudiante)
        self.estudianteRepositorio.save(Estudiante)
        return elEstudiante.__dict__
    def show(self, id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
    def show2(self, id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        Estudiantes = self.estudianteRepositorio.findAll()
        return elEstudiante.__dict__

    def update(self, id, infoEstudiante):
        print("Actualizando estudiante con id ", id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return {"deleted_count": 1}