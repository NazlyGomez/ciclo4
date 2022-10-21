from Modelos.ModeloResultado import Resultado

class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")
    def index(self):
        print("Listar todos los resultados de la mesa ")
        UnaMesa = {
            "ID": "ABC123",
            "Numero de la mesa": "10",
            "Cedula del candidato": "12345678",
            "Numero de votos": "200",
        }
        return [UnaMesa]

    def create(self,infoResultado):
        print("Crear un Resultado")
        ElResultado = Resultado (infoResultado)
        return ElResultado.__dict__

    def show(self, ID):
        print("Mostrando el resultado de la mesa con ID ", ID)
        ElResultado = {
            "ID": "ABC123",
            "Numero de la mesa": "10",
            "Cedula del candidato": "12345678",
            "Numero de votos": "200",
        }
        return [ElResultado]

    def update(self, ID, infoResultado):
        print("Actualizando el resultado de la mesa con ID ", ID)
        ElResultado = Resultado(infoResultado)
        return  ElResultado.__dict__

    def delete(self, ID):
        print("Eliminando resultado de la mesa con ID ", ID)
        return {"deleted_count": 1}