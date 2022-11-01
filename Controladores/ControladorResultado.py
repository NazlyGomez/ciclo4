from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPersona import RepositorioPersona
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Persona import Persona


class ControladorResultado():

    def __init__(self):
        self.resultadorepositorio = RepositorioResultado()
        self.mesarepositorio=RepositorioMesa()
        self.personarepositorio=RepositorioPersona()

    def index(self):
        return self.resultadorepositorio.findAll()

    def create(self, infoResultado,id_Persona,id_Mesa):
        nuevoResultado=Resultado(infoResultado)
        lapersona=Persona(self.personarepositorio.findById(id_Persona))
        lamesa = Mesa(self.mesarepositorio.findById(id_Mesa))
        nuevoResultado.Persona=lapersona
        nuevoResultado.Mesa = lamesa
        return (self.resultadorepositorio.save(nuevoResultado))

    def show(self, id_Resultado):
        elResultado = Resultado(self.resultadorepositorio.findById(id_Resultado))
        return elResultado.__dict__

    def update(self, id_Resultado, infoResultado,id_Persona,id_Mesa):
        elResultado=Resultado(self.resultadorepositorio.findById(id_Resultado))
        elResultado.NumeroMesa=infoResultado["NumeroMesa"]
        elResultado.CedulaCandidato = infoResultado["CedulaCandidato"]
        elResultado.NumeroVotos = infoResultado["NumeroVotos"]
        lapersona = Persona(self.personarepositorio.findById(id_Persona))
        lamesa = Mesa(self.mesarepositorio.findById(id_Mesa))
        elResultado.Persona=lapersona
        elResultado.Mesa=lamesa
        return (self.resultadorepositorio.save(elResultado))

    def delete(self, id_Resultado):
        return self.resultadorepositorio.delete(id_Resultado)