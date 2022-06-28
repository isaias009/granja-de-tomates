REGLAS = {
  'sin-tomate': 'pedir-tomate',
  'con-tomate': 'revisar',
  'tomate-maduro': 'preparar-venta',
  'tomate-podrido': 'desechar',
  'tomate-no-maduro': 'almacenar'
}

MODELO = {
  ('sin-tomate', 'pedir-tomate', 'tomate'): 'con-tomate',
  ('con-tomate', 'revisar', 'maduro'): 'tomate-maduro',
  ('con-tomate', 'revisar', 'podrido'): 'tomate-podrido',
  ('con-tomate', 'revisar', 'no-maduro'): 'tomate-no-maduro',
  ('tomate-maduro', 'preparar-venta', 'revisado'): 'sin-tomate',
  ('tomate-podrido', 'desechar', 'revisado'): 'sin-tomate',
  ('tomate-no-maduro', 'almacenar', 'revisado'): 'sin-tomate',
}