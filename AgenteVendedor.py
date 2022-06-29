# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:25:41 2022

@author: Nico
"""



REGLAS =  {  
  # Agente vendedor
  'comprar' : 'vender_tomate',
  'preguntar' : 'responder_si_hay_disponible',
  'facturar'  : 'pagar',
}

#%% 
class AgenteReactivoSimple:
    """Agente racional de tipo reactivo simple"""
    def __init__(self, reglas):
        self.reglas =reglas
      
    def actuar(self, percepcion, accion_basica=''):
        """ Actua en base a una percepción y una acción básica."""
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        return accion_basica
   
   
#%%

#%%

# print("-- Agente Vendedor --")
# agente = AgenteReactivoSimple(REGLAS)
# percepcion = input("Introduce una percepcion: ")
# while percepcion:
#     action = agente.actuar(percepcion, 'esperar')
#     print("Accion: ", action)
#     percepcion = input("Introduce una percepcion: ")