from modelo import AgenteReactivoBasadoModelo
from flask import jsonify

REGLAS = {
  'sin_semillas': 'obtener_semillas',
  'con_semillas': 'verificar_estacion',
  'estacion_primavera': 'preparar_huerto',
  'estacion_invierno': 'verificar_estacion',
  'estacion_otonio': 'verificar_estacion',
  'estacion_verano': 'verificar_estacion',
  'huerto_listo': 'sembrar_semillas',
  'semillas_sembradas': 'verificar_humedad',
  'huerto_seco': 'regar_huerto',
  'huerto_humedo': 'esperar',
  'semillas_germinadas': 'trasladar_semillas',
  'semillas_trasladadas': 'esperar',
  'tomate_listo': 'recoger_tomates'
}

MODELO = {
  ('sin_semillas','obtener_semillas', 'semillas'): 'con_semillas',
  ('con_semillas','verificar_estacion', 'primavera'): 'estacion_primavera',
  ('con_semillas','verificar_estacion', 'invierno'): 'estacion_invierno',
  ('con_semillas','verificar_estacion', 'otonio'): 'estacion_otonio',
  ('con_semillas','verificar_estacion', 'verano'): 'estacion_verano',
  ('estacion_invierno', 'verificar_estacion', 'primavera'): 'estacion_primavera',
  ('estacion_otonio', 'verificar_estacion', 'primavera'): 'estacion_primavera',
  ('estacion_verano', 'verificar_estacion', 'primavera'): 'estacion_primavera',
  ('estacion_primavera', 'preparar_huerto', 'huerto'): 'huerto_listo',
  ('huerto_listo', 'sembrar_semillas', 'sembrado'): 'semillas_sembradas',
  ('semillas_sembradas', 'verificar_humedad', 'seco'): 'huerto_seco',
  ('semillas_sembradas', 'verificar_humedad', 'humedo'): 'huerto_humedo',
  ('huerto_seco', 'regar_huerto', 'humedo'): 'huerto_humedo',
  ('huerto_humedo', 'esperar', 'germinadas'): 'semillas_germinadas',
  ('semillas_germinadas', 'trasladar_semillas', 'traslado'): 'semillas_trasladadas',
  ('semillas_trasladadas', 'esperar', 'tomate'): 'tomate_listo',
  ('tomate_listo', 'recoger_tomates', 'obtenido'): 'sin_semillas',
}

class AgenteAgricultor:

  def __init__(self, pasos):
    self.pasos = pasos
    self.agente = AgenteReactivoBasadoModelo(MODELO, REGLAS, 'sin_semillas', 'obtener_semillas')

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


# print("-- Agente Agricultor --")
# agricultor = AgenteReactivoBasadoModelo(MODELO, REGLAS, 'sin_semillas', 'obtener_semillas')
# percepcion = input("Indicar Percepcion: ")
# while percepcion:
#   accion = agricultor.actuar(percepcion)
#   print(accion)
#   percepcion = input("Indicar Percepcion: ")
