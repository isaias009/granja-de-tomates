from flask import Flask, request
from flask_cors import CORS
from AgenteAgricultor import AgenteAgricultor
from AgenteCalidad import AgenteCalidad
from AnalisisTomate import AnalizarTomate


app = Flask(__name__)
CORS(app)

# -- Agente control de calidad --
@app.route('/control-de-calidad', methods=['POST'])
def ControlCalidad():
  data = request.json
  agente = AgenteCalidad(data['pasos'])
  return agente.accion()

# -- Agente agricultor --
@app.route('/agricultor', methods=['POST'])
def Granjero():
  data = request.json
  agente = AgenteAgricultor(data['pasos'])
  return agente.accion()

if __name__ == '__main__':
  app.run(debug=True, port=4000)