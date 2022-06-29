from AgenteVendedor import AgenteReactivoSimple, REGLAS as REGLAS_V
from AgenteAgricultor import MODELO as MODELO_A, REGLAS as REGLAS_A
from AgenteCalidad import MODELO as MODELO_C, REGLAS as REGLAS_C
from modelo import AgenteReactivoBasadoModelo

class MultiAgentes:

  def __init__(self):
    pass

  def interactuarAgentes(self):
    print("-- Agente Agricultor --")
    agricultor = AgenteReactivoBasadoModelo(MODELO_A, REGLAS_A, 'sin_semillas', 'obtener_semillas')
    accionesAgricultor = ["semillas","primavera","huerto","sembrado","seco"]
    for accion in accionesAgricultor:
      respuesta = agricultor.actuar(accion)
      print(respuesta)
    
    print("-- Agente Control de calidad --")
    inspeccionador = AgenteReactivoBasadoModelo(MODELO_C, REGLAS_C, 'sin_tomate', 'pedir_tomate')
    accionesAgenteCalidad = ["tomate","maduro","revisado","tomate","no_maduro","revisado","tomate","podrido","revisado"]
    for accion in accionesAgenteCalidad:
      respuesta = inspeccionador.actuar(accion)
      print(respuesta)

    print("-- Agente Vendedor --")
    agenteVendedor = AgenteReactivoSimple(REGLAS_V)
    accionesAgenteVendedor = ["preguntar","comprar","facturar"]
    for accion in accionesAgenteVendedor:
      respuesta = agenteVendedor.actuar(accion)
      print(respuesta)

multiagentes = MultiAgentes()

multiagentes.interactuarAgentes()