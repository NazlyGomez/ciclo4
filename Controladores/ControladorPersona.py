from Repositorios.RepositorioPersona import RepositorioPersona
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Persona import Persona
from Modelos.Partido import Partido


class ControladorPersona():

    def __init__(self):
        self.personarepositorio = RepositorioPersona()
        self.partidorepositorio=RepositorioPartido()
    def index(self):
        return self.personarepositorio.findAll()

    def create(self, infoPersona):
        nuevaPersona = Persona(infoPersona)
        return self.personarepositorio.save(nuevaPersona)

    def show(self, id_Persona):
        laPersona = Persona(self.personarepositorio.findById(id_Persona))
        return laPersona.__dict__

    def update(self, id_Persona, infoPersona):
       personaActual = Persona(self.personarepositorio.findById(id_Persona))
       personaActual.Cedula = infoPersona["Cedula"]
       personaActual.NumeroResolucion = infoPersona["NumeroResolucion"]
       personaActual.Nombres = infoPersona["Nombres"]
       personaActual.Apellidos = infoPersona["Apellidos"]

       return self.personarepositorio.save(personaActual)

    def delete(self, id_Persona):
        return self.personarepositorio.delete(id_Persona)

    "Relacion entre persona y partido"

    def asignarPartido(self, id_Persona, id_Partido):
        personaActual = Persona(self.personarepositorio.findById(id_Persona))
        partidoActual = Partido(self.partidorepositorio.findById(id_Partido))
        personaActual.Partido = partidoActual
        return self.personarepositorio.save(personaActual)





