from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa


class ControladorMesa():

    def __init__(self):
        self.mesarepositorio = RepositorioMesa()

    def index(self):
        return self.mesarepositorio.findAll()

    def create(self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.mesarepositorio.save(nuevaMesa)

    def show(self, id_Mesa):
        lamesa = Mesa(self.mesarepositorio.findById(id_Mesa))
        return lamesa.__dict__

    def update(self, id_Mesa, infoMesa):
       mesaActual = Mesa(self.mesarepositorio.findById(id_Mesa))
       mesaActual.Codigo = infoMesa["Codigo"]
       mesaActual.CantidadInscritos = infoMesa["CantidadInscritos"]
       return self.mesarepositorio.save(mesaActual)

    def delete(self, id_Mesa):
        return self.mesarepositorio.delete(id_Mesa)
