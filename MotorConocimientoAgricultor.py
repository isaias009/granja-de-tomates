from experta import *
from datetime import datetime, date, time

class Entorno(Fact):
  """Informacion acerca del entorno del agente agricultor"""
  pass

class Cultivo(Fact):
  """Informacion acerca del cultivo del agente agricultor"""
  pass


class MotorConocimientoAgricultor(KnowledgeEngine):
  @Rule(Entorno(temperatura=P(lambda x: x >= 18) & P(lambda x: x <= 27)), salience = 3)
  def temperatura_adecuada(self):
    print("temperatura_adecuada")

  @Rule(Entorno(temperatura=P(lambda x: x < 18) | P(lambda x: x > 27)), salience = 3)
  def temperatura_inadecuada(self):
    print("temperatura_inadecuada")

  @Rule(Entorno(fecha=P(lambda x: x >= date(2022,3,20)) & P(lambda x: x <= date(2022,6,21))), salience = 4)
  def estacion_otonio(self):
    print("estacion_otonio")

  @Rule(Entorno(fecha=P(lambda x: x > date(2022,6,21)) & P(lambda x: x < date(2022,9,21))), salience = 4)
  def estacion_invierno(self):
    print("estacion_invierno")

  @Rule(Entorno(fecha=P(lambda x: x >= date(2022,9,21)) & P(lambda x: x <= date(2022,12,20))), salience = 4)
  def estacion_primavera(self):
    print("estacion_primavera")

  @Rule(Entorno(fecha=P(lambda x: x > date(2022,12,20)) & P(lambda x: x < date(2023,3,20))), salience = 4)
  def estacion_verano(self):
    print("estacion_verano")

  @Rule(Entorno(hora=P(lambda x: x >= time(6,0,0)) & P(lambda x: x <= time(18,30,0))), salience = 2)
  def es_de_dia(self):
    print("es_de_dia")

  @Rule(Entorno(hora=P(lambda x: x < time(6,0,0)) | P(lambda x: x > time(18,30,0))), salience = 2)
  def es_de_noche(self):
    print("es_de_noche")

  @Rule(Entorno(suelo=L("seco")), salience = 1)
  def suelo_seco(self):
    print("suelo_seco")

  @Rule(Entorno(suelo=L("humedo")), salience = 1)
  def suelo_humedo(self):
    print("suelo_humedo")

  @Rule(Cultivo(semillas=P(lambda x: x > 0)), salience = 5)
  def con_semillas(self):
    print("con_semillas")

  @Rule(Cultivo(semillas=P(lambda x: x == 0)), salience = 5)
  def sin_semillas(self):
    print("sin_semillas")

  @Rule(Cultivo(plantines=P(lambda x: x > 0)), salience = 5)
  def con_plantines(self):
    print("con_plantines")

  @Rule(Cultivo(plantines=P(lambda x: x == 0)), salience = 5)
  def sin_plantines(self):
    print("sin_plantines")

  def evaluar(self, declaraciones):
    self.reset()

    if 'temperatura' in declaraciones.keys():
      valorTemperatura = declaraciones['temperatura']
      self.declare(Entorno(temperatura=valorTemperatura))

    if 'fecha' in declaraciones.keys():
      cadenaFecha = declaraciones['fecha']
      elementosFecha = cadenaFecha.split('/')
      day = int(elementosFecha[0])
      month = int(elementosFecha[1])
      year = int(elementosFecha[2])
      objetoFecha = date(year,month,day)
      self.declare(Entorno(fecha=objetoFecha))

    if 'hora' in declaraciones.keys():
      cadenaHora = declaraciones['hora']
      elementosHora = cadenaHora.split(":")
      horaInt = int(elementosHora[0])
      minutoInt = int(elementosHora[1])
      segundosInt = int(elementosHora[2])
      objetoHora = time(horaInt,minutoInt,segundosInt)
      self.declare(Entorno(hora=objetoHora))

    if 'suelo' in declaraciones.keys():
      estadoSuelo = declaraciones['suelo']
      self.declare(Entorno(suelo=estadoSuelo))

    if 'plantines' in declaraciones.keys():
      cantidadPlantines = declaraciones['plantines']
      self.declare(Cultivo(plantines=cantidadPlantines))

    if 'semillas' in declaraciones.keys():
      cantidadSemillas = declaraciones['semillas']
      self.declare(Cultivo(semillas=cantidadSemillas))


  def ejecutar(self, steps=float('inf')):
      """
      Execute agenda activations
      """
      self.history = []
      self.running = True
      activation = None
      execution = 0
      while steps > 0 and self.running:

          added, removed = self.get_activations()
          self.strategy.update_agenda(self.agenda, added, removed)

          if watchers.worth('AGENDA', 'DEBUG'):  # pragma: no cover
              for idx, act in enumerate(self.agenda.activations):
                  watchers.AGENDA.debug(
                      "%d: %r %r",
                      idx,
                      act.rule.__name__,
                      ", ".join(str(f) for f in act.facts))

          activation = self.agenda.get_next()

          if activation is None:
              break
          else:
              steps -= 1
              execution += 1

              self.history.append(activation.rule.__name__)

              watchers.RULES.info(
                  "FIRE %s %s: %s",
                  execution,
                  activation.rule.__name__,
                  ", ".join(str(f) for f in activation.facts))
              
        
              activation.rule(
                  self,
                  **{k: v
                      for k, v in activation.context.items()
                      if not k.startswith('__')})

      self.running = False
      return tuple(self.history)