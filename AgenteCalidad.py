from modelo import AgenteReactivoBasadoModelo
from flask import jsonify

REGLAS = {
  'sin_tomate': 'pedir_tomate',
  'con_tomate': 'revisar',
  'tomate_maduro': 'preparar_venta',
  'tomate_podrido': 'desechar',
  'tomate_no-maduro': 'almacenar'
}

MODELO = {
  ('sin_tomate', 'pedir_tomate', 'tomate'): 'con_tomate',
  ('con_tomate', 'revisar', 'maduro'): 'tomate_maduro',
  ('con_tomate', 'revisar', 'podrido'): 'tomate_podrido',
  ('con_tomate', 'revisar', 'no_maduro'): 'tomate_no_maduro',
  ('tomate_maduro', 'preparar_venta', 'revisado'): 'sin_tomate',
  ('tomate_podrido', 'desechar', 'revisado'): 'sin_tomate',
  ('tomate_no-maduro', 'almacenar', 'revisado'): 'sin_tomate',
}

class AgenteCalidad:

  def __init__(self, pasos):
    self.pasos = pasos
    self.agente = AgenteReactivoBasadoModelo(MODELO, REGLAS, 'sin_tomate', 'pedir_tomate')

  def accion(self):
    if(len(self.pasos) > 0):
      accion = ''

      for x in self.pasos:
        accion = self.agente.actuar(x)

      return jsonify({
        "message": accion
      }) 

    else:
      return jsonify({
        "message": self.agente.actuar('')
      })
