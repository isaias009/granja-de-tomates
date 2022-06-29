REGLAS_A = {
  'sin-semillas':'obtener-semillas',
  'con-semillas':'verificar-estacion',
  'estacion-primavera':'preparar-huerto',
  'estacion-invierno':'esperar-primavera',
  'estacion-otonio':'esperar-primavera',
  'estacion-verano':'esperar-primavera',
  'huerto-listo': 'sembrar-semillas',
  'huerto-seco': 'regar-huerto',
  'semillas-germinadas': 'trasladar-huerto',
  'tomate-listo': 'recoger-tomates'
}

MODELO_A = {
  ('sin-semillas','obtener-semillas', 'semillas'): 'con-semillas',
  ('con-semillas','verificar-estacion', 'primavera'): 'estacion-primavera',
  ('con-semillas','verificar-estacion', 'invierno'): 'estacion-invierno',
  ('con-semillas','verificar-estacion', 'otonio'): 'estacion-otonio',
  ('con-semillas','verificar-estacion', 'verano'): 'estacion-verano',
  ('estacion-primavera', 'preparar-huerto', 'huerto'): 'huerto-listo',
  ('estacion-invierno', 'esperar-primavera', 'semillas'): 'con-semillas',
  ('estacion-otonio', 'esperar-primavera', 'semillas'): 'con-semillas',
  ('estacion-verano', 'esperar-primavera', 'semillas'): 'con-semillas',
  ('huerto-listo', 'sembrar-semillas', 'sembrado-listo'): 'huerto-seco',
  ('huerto-seco', 'regar-huerto', 'seco'): 'huerto-humedo',
}