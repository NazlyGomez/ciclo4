from Modelos.ModeloPersona import Persona


class ControladorPersona():
    def __init__(self):
        print("Creando ControladorPersona")
    def index(self):
        print("Listar todas las personas ")
        UnaPersona = {
            "Cedula": "12345678",
            "Nombres": "Juan Sebastian",
            "Apellidos": "Guevara Cruz",
            "Nresolucion": "987654",
        }
        return [UnaPersona]

    def create(self,infoPersona):
        print("Crear una Persona")
        Lapersona = Persona (infoPersona)
        return Lapersona.__dict__

    def show(self, Cedula):
        print("Mostrando una persona con cedula ", Cedula)
        Lapersona = {
            "Cedula": "12345678",
            "Nombres": "Juan Sebastian",
            "Apellidos": "Guevara Cruz",
            "Nresolucion": "987654",
        }
        return [Lapersona]

    def update(self, Cedula, infoPersona):
        print("Actualizando datos de la persona con cedula ", Cedula)
        Lapersona = Persona(infoPersona)
        return  Lapersona.__dict__

    def delete(self, Cedula):
        print("Eliminando Partido con codigo ", Cedula)
        return {"deleted_count": 1}