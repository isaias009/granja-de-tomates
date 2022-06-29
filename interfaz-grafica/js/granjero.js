import { 

  ObtenerSemillas, 
  VerificarEstacion, 
  PrepararHuerto, 
  SembrarSemillas,
  VerificarHumedad

} from './huerto.js'

export const agenteGranjero = async(URL, arreglo) => {
  return await fetch(`${URL}/agricultor`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      pasos: arreglo
    })
  });
}

export const showRegadera = () => {
  const granjero = document.createElement('img');
  const huerto = document.getElementById('huerto');

  granjero.src = '../img/animations/regar.gif';
  granjero.className = 'granjero';
  granjero.id = 'regadera'

  huerto.appendChild(granjero);
}


export const hiddenRegadera = () => {
  const granjero = document.getElementById('regadera');
  granjero.parentNode.removeChild(granjero);
}

export const showGranjero = () => {
  const granjero = document.createElement('img');
  const huerto = document.getElementById('huerto');

  granjero.src = '../img/animations/podar.gif';
  granjero.className = 'granjero';
  granjero.id = 'granjero'

  huerto.appendChild(granjero);
}


export const hiddenGranjero = () => {
  const granjero = document.getElementById('granjero');
  granjero.parentNode.removeChild(granjero);
}


export const acciones = (value) => {
  console.log(value);
  const options = {
    'obtener_semillas': ObtenerSemillas,
    'verificar_estacion': VerificarEstacion,
    'preparar_huerto': PrepararHuerto,
    'sembrar_semillas': SembrarSemillas,
    'verificar_humedad': VerificarHumedad
  }

  return options[value]();
}