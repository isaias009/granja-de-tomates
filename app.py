from flask import Flask, jsonify, request
from modelo import AgenteReactivoBasadoModelo
from AgenteCalidad import REGLAS, MODELO


app = Flask(__name__)


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



@app.route('/agricultor', methods=['POST'])
def Agricultor():
  #Condigo agricultor
  pass
  

if __name__ == '__main__':
  app.run(debug=True, port=4000)