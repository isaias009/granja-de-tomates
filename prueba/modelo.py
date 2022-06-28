REGLAS = {
  'sin-moneda': 'pedir-moneda',
  'con-moneda': 'pedir-codigo',
  'a1-servida': 'esperar',
  'a2-servida': 'esperar',
  'a3-servida': 'esperar'
}

MODELO = {
  ('sin-moneda', 'pedir-moneda', 'moneda'): 'con-moneda',
  ('con-moneda', 'pedir-codigo', 'a1'): 'a1-servida',
  ('con-moneda', 'pedir-codigo', 'a2'): 'a2-servida',
  ('con-moneda', 'pedir-codigo', 'a3'): 'a3-servida',
  ('a1-servida', 'esperar', 'servida'): 'sin-moneda',
  ('a2-servida', 'esperar', 'servida'): 'sin-moneda',
  ('a3-servida', 'esperar', 'servida'): 'sin-moneda',
}

class AgenteModelo:

  def __init__(self, modelo, reglas, estado_inicial='', accion_inicial=''):
    self.modelo = modelo
    self.reglas = reglas
    self.estado_inicial = estado_inicial
    self.accion_inicial = accion_inicial
    self.accion = None
    self.estado = self.estado_inicial
    self.ultima_accion = self.accion_inicial
  
  def actuar(self, percepcion):
    if not percepcion:
      return self.accion_inicial

    clave = (self.estado, self.ultima_accion, percepcion)
    if clave not in self.modelo.keys():
      self.accion = None
      self.estado = self.estado_inicial
      self.ultima_accion = self.accion_inicial
      return self.accion_inicial

    self.estado = self.modelo[clave]
    if self.estado not in self.reglas.keys():
      self.accion = None
      self.estado = self.estado_inicial
      self.ultima_accion = self.accion_inicial
      return self.accion_inicial

    accion = self.reglas[self.estado]
    self.ultima_accion = accion
    return accion


print("Agente")
expendedora = AgenteModelo(MODELO, REGLAS, 'sin-moneda', 'pedir-moneda')
percepcion = input("Indicar Percepcion: ")
while percepcion:
  accion = expendedora.actuar(percepcion)
  print(accion)
  percepcion = input("Indicar Percepcion: ")