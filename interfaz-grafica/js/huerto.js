import {
  showRegadera,
  hiddenRegadera,
  showGranjero, 
  hiddenGranjero, 
  agenteGranjero, 
  acciones 
} from './granjero.js'

const URL = 'http://127.0.0.1:4000'

export const VerificarHumedad = () => {
  const regar = document.getElementById('regar');
  const huerto = document.getElementById('huerto');
  regar.style.display = 'inline-block';

  regar.addEventListener('click', () => {

    const cubos = Array.from(huerto.children);

    showRegadera();
    setTimeout(() => {
      hiddenRegadera();
    }, 2000);

    agenteGranjero(URL, ["semillas", "primavera", "huerto", "sembrado", "humedo"])
      .then((response) => response.json())
      .then((data) => {
        acciones(data.message)
      });

    setTimeout(() => {
      cubos.forEach((item, index) => {
        item.innerHTML = '';
        const semillas = document.createElement('img');
        semillas.src = '../img/germinado.png';
        semillas.id = 'germinado-'+index;
        semillas.className = 'germinado';
        item.appendChild(semillas);
      });
    }, 2000);
    
    regar.style.display = 'none';
  });
}

export const SembrarSemillas = () => {
  const sembrar = document.getElementById('sembrar-semillas');
  const huerto = document.getElementById('huerto');
  const semillas = document.getElementById('semillas');
  sembrar.style.display = 'inline-block';
  
  sembrar.addEventListener('click', () => {
    
    const cubos = Array.from(huerto.children);
    semillas.style.display = 'none';

    cubos.forEach((item, index) => {
      item.innerHTML = '';
      const semillas = document.createElement('img');
      semillas.src = '../img/semilla.png';
      semillas.id = 'semilla-'+index;
      semillas.className = 'semillas';
      item.appendChild(semillas);
    });

    agenteGranjero(URL, ["semillas", "primavera", "huerto", "sembrado"])
      .then((response) => response.json())
      .then((data) => {
        acciones(data.message)
      });

    sembrar.style.display = 'none';
  });
}

export const PrepararHuerto = () => {
  const preparar = document.getElementById('preparar-huerto');
  const huerto = document.getElementById('huerto');

  preparar.style.display = 'inline-block';

  preparar.addEventListener('click', () => {

    const cubos = Array.from(huerto.children);

    showGranjero();
    setTimeout(() => {
      cubos.forEach((item) => {
        item.className = 'tierra'
      });
      hiddenGranjero();
    }, 2000);

    agenteGranjero(URL, ["semillas", "primavera", "huerto"])
      .then((response) => response.json())
      .then((data) => {
        acciones(data.message)
      });
    
    preparar.style.display = 'none';
  });
}

export const ObtenerSemillas = () => {
  const herr = document.getElementById('herr')
  const obtener = document.getElementById('obtener-semillas');
  const semillas = document.createElement('img');
  
  obtener.style.display = 'inline-block'

  semillas.src = '../img/semillas.jpg';
  semillas.id = 'semillas';
  semillas.className = 'semillas';

  obtener.addEventListener('click', () => {
    herr.appendChild(semillas);
    agenteGranjero(URL, ["semillas"])
      .then((response) => response.json())
      .then((data) => {
        acciones(data.message)
      });
    obtener.style.display = 'none'
  });
}


export const VerificarEstacion = () => {
  const verificar = document.getElementById('verificar-estacion');
  const estacion = document.getElementById('estacion');
  verificar.style.display = 'inline-block'

  verificar.addEventListener('click', () => {
    agenteGranjero(URL, ["semillas", (estacion.textContent).toLowerCase()])
      .then((response) => response.json())
      .then((data) => {
        acciones(data.message)
      });
      verificar.style.display = 'none'
  });
}