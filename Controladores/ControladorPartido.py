from Modelos.ModeloPartido import Partido


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")
    def index(self):
        print("Listar todas los Partidos")
        UnPartido = {
            "Codigo": "1234",
            "Nombre": "Partido union patriotica",
            "Lema": "Unidos somos mas",
        }
        return [UnPartido]

    def create(self,infoPartido):
        print("Crear un Partido")
        Elpartido = Partido (infoPartido)
        return Elpartido.__dict__

    def show(self, Codigo):
        print("Mostrando un partido con codigo ", Codigo)
        Elpartido = {
            "Codigo": "1234",
            "Nombre": "Partido union patriotica",
            "Lema": "Unidos somos mas",
        }
        return [Elpartido]

    def update(self, Codigo, infoPartido):
        print("Actualizando Partido con codigo ", Codigo)
        Elpartido = Partido(infoPartido)
        return  Elpartido.__dict__

    def delete(self, Codigo):
        print("Eliminando Partido con codigo ", Codigo)
        return {"deleted_count": 1}