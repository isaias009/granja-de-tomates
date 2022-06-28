ACCIONES = {
  'moneda': 'pedir-codigo',
  'moneda,a1': 'servir-bebida1',
  'moneda,a3': 'servir-bebida2'
}


class AgenteTabla:
  """ Aegnte de tipo tabla """

  def __init__(self, acciones):
    self.acciones = acciones
    self.percepciones = ""

  def actuar(self, percepcion, accion_basica=''):
    """Actua segun la percepcion"""
    if not percepcion:
      return accion_basica

    if len(self.percepciones) != 0:
      self.percepciones += ','
    self.percepciones += percepcion

    if self.percepciones in self.acciones.keys():
      return self.acciones[self.percepciones]

    self.percepciones = ''
    return accion_basica

print("-- Agente --")
expendedora = AgenteTabla(ACCIONES)
percepcion = input("Indicar Percepcion: ")

while percepcion :
  accion = expendedora.actuar(percepcion, 'esperar')
  print(accion)
  percepcion = input("indicar Percepcion: ")