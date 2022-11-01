from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido


class ControladorPartido():

    def __init__(self):
        self.partidorepositorio = RepositorioPartido()

    def index(self):
        return self.partidorepositorio.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.partidorepositorio.save(nuevoPartido)

    def show(self, id_Partido):
        elpartido = Partido(self.partidorepositorio.findById(id_Partido))
        return elpartido.__dict__

    def update(self, id_Partido, infoPartido):
       partidoActual = Partido(self.partidorepositorio.findById(id_Partido))
       partidoActual.Nombre = infoPartido["Nombre"]
       partidoActual.Lema = infoPartido["Lema"]
       return self.partidorepositorio.save(partidoActual)

    def delete(self, id_Partido):
        return self.partidorepositorio.delete(id_Partido)
