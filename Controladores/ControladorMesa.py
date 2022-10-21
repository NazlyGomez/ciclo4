from Modelos.ModeloMesa import Mesa


class ControladorMesa:
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las Mesas")
        UnaMesa = {
            "Codigo": "1234",
            "Cantidad inscritos": "100",
        }
        return [UnaMesa]

    def create(self,infoMesa):
        print("Crear una Mesa")
        Lamesa = Mesa (infoMesa)
        return Lamesa.__dict__

    def show(self, Codigo):
        print("Mostrando una mesa con codigo ", Codigo)
        Lamesa = {
            "Codigo": "1234",
            "Cantidad inscritos": "100"
        }
        return [Lamesa]

    def update(self, Codigo, infoMesa):
        print("Actualizando Mesa con codigo ", Codigo)
        Lamesa = Mesa(infoMesa)
        return Lamesa.__dict__

    def delete(self, Codigo):
        print("Eliminando Mesa con codigo ", Codigo)
        return {"deleted_count": 1}