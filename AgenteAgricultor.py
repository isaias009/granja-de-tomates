from datetime import datetime
from MotorConocimientoAgricultor import MotorConocimientoAgricultor
# Estados = 
# sin_semillas, con_semillas, estacion_primavera, estacion_invierno, estacion_otonio, estacion_verano

# Acciones = 


REGLAS = {
  'sin_tomate': 'pedir_tomate',
  'con_tomate': 'revisar',
  'tomate_maduro': 'preparar_venta',
  'tomate_podrido': 'desechar',
  'tomate_no_maduro': 'almacenar'
}

MODELO = {
  ('sin_tomate', 'pedir_tomate', 'tomate'): 'con_tomate',
  ('con_tomate', 'revisar', 'maduro'): 'tomate_maduro',
  ('con_tomate', 'revisar', 'podrido'): 'tomate_podrido',
  ('con_tomate', 'revisar', 'no_maduro'): 'tomate_no_maduro',
  ('tomate_maduro', 'preparar_venta', 'revisado'): 'sin_tomate',
  ('tomate_podrido', 'desechar', 'revisado'): 'sin_tomate',
  ('tomate_no_maduro', 'almacenar', 'revisado'): 'sin_tomate',
  ('con_semillas','estacion_primavera','temperatura_adecuada','es_de_dia'): 'germinar',
  ('con_plantines','estacion_primavera','temperatura_adecuada','es_de_dia'): 'plantar',
}

tiempo = datetime.now()
horaActual = tiempo.strftime("%H:%M:%S")
motorConocimientoAgricultor = MotorConocimientoAgricultor()
motorConocimientoAgricultor.evaluar({'semillas':100,'fecha':'21/9/2022','hora':'15:0:0','temperatura':27})
resultadoEjecucion = motorConocimientoAgricultor.ejecutar()
print("Accion: ")
print(MODELO[resultadoEjecucion])
