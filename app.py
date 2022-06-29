from flask import Flask, jsonify, request
from flask_cors import CORS
from modelo import AgenteReactivoBasadoModelo
from AgenteCalidad import REGLAS, MODELO
from AgenteAgricultor import REGLAS_A, MODELO_A
from AnalisisTomate import AnalizarTomate


app = Flask(__name__)
CORS(app)

@app.route('/control-de-calidad', methods=['POST'])
def ControlCalidad():
  data = request.json

  expendedora = AgenteReactivoBasadoModelo(MODELO, REGLAS, 'sin-tomate', 'pedir-tomate')
  
  if(len(data['pasos']) > 0):
    accion = ''

    for x in data['pasos']:
      accion = expendedora.actuar(x)

    return jsonify({
      "message": accion
    }) 

  else:
    return jsonify({
      "message": expendedora.actuar('')
    })


@app.route('/granjero', methods=['POST'])
def Granjero():
  data = request.json

  expendedora = AgenteReactivoBasadoModelo(MODELO_A, REGLAS_A, 'sin-semillas', 'obtener-semillas')
  
  if(len(data['pasos']) > 0):
    accion = ''

    for x in data['pasos']:
      accion = expendedora.actuar(x)

    return jsonify({
      "message": accion
    }) 

  else:
    return jsonify({
      "message": expendedora.actuar('')
    })

if __name__ == '__main__':
  app.run(debug=True, port=4000)