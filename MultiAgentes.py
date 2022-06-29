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
    percepcion = input("Indicar Percepcion: ")
    while percepcion:
      accion = agricultor.actuar(percepcion)
      print(accion)
      percepcion = input("Indicar Percepcion: ")

    # print("-- Agente Vendedor --")
    # agente = AgenteReactivoSimple(REGLAS_V)
    # percepcion = input("Introduce una percepcion: ")
    # while percepcion:
    #     action = agente.actuar(percepcion, 'esperar')
    #     print("Accion: ", action)
    #     percepcion = input("Introduce una percepcion: ")

    # print("-- Agente Control de calidad --")
    # control_calidad = AgenteReactivoBasadoModelo(MODELO_C, REGLAS_C, 'sin_tomate', 'pedir_tomate')
    # percepcion = input("Indicar Percepcion: ")
    # while percepcion:
    #   accion = control_calidad.actuar(percepcion)
    #   print(accion)
    #   percepcion = input("Indicar Percepcion: ")

multiagentes = MultiAgentes()

multiagentes.interactuarAgentes()