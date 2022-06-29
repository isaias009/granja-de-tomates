import { acciones, agenteGranjero } from './granjero.js'

const URL = 'http://127.0.0.1:4000';

const tiempoDeIA = (velocidad, fecha_inicial = null) => {
  const fechaHtml = document.getElementById('fecha');
  const horaHtml = document.getElementById('hora');
  
  moment.locale('es', {
      months: 'Enero_Febrero_Marzo_Abril_Mayo_Junio_Julio_Agosto_Septiembre_Octubre_Noviembre_Diciembre'.split('_'),
      monthsShort: 'Enero._Feb._Mar_Abr._May_Jun_Jul._Ago_Sept._Oct._Nov._Dec.'.split('_'),
      weekdays: 'Domingo_Lunes_Martes_Miercoles_Jueves_Viernes_Sabado'.split('_'),
      weekdaysShort: 'Dom._Lun._Mar._Mier._Jue._Vier._Sab.'.split('_'),
      weekdaysMin: 'Do_Lu_Ma_Mi_Ju_Vi_Sa'.split('_')
    }
  );

  let hora = Number(moment().format('H'));
  let fecha = fecha_inicial ? moment(fecha_inicial) : moment();
  
  fechaHtml.dataset.fecha = fecha;
  fechaHtml.innerHTML = fecha.format('DD [de] MMMM [del] YYYY');
  horaHtml.innerHTML = hora <= 9 ? `0${hora}`: hora;

  return setInterval(() => {

    fechaHtml.dataset.fecha = fecha;
    fechaHtml.innerHTML = fecha.format('DD [de] MMMM [del] YYYY');
    horaHtml.innerHTML = hora <= 9 ? `0${hora}`: hora;
    hora++;

    estaciones(fecha.format('YYYY-MM-DD'));
    
    if(hora > 23){
      hora = 0;
      fecha.add(5, 'days').calendar();
    }
  
  }, velocidad);
}


const estaciones = (fecha) => {
  const actual = moment(fecha);
  const primavera = moment(fecha).set({date: 22, month: 8});
  const invierno = moment(fecha).set({date: 21, month: 5});
  const otonio = moment(fecha).set({date: 20, month: 2});
  const estacion = document.getElementById('estacion');

  if(actual.diff(primavera, 'day') >= 0){
    estacion.textContent = 'Primavera';
    document.body.style.backgroundImage = "url('../img/fondo/fondo-granja.jpg')";
  }else if(actual.diff(invierno, 'day') >= 0){
    estacion.textContent = 'Invierno';
    document.body.style.backgroundImage = "url('../img/fondo/granja-invierno.jpg')";
  }else if(actual.diff(otonio, 'day') >= 0){
    estacion.textContent = 'Otoño';
    document.body.style.backgroundImage = "url('../img/fondo/granja-otono.jpg')";
  }else{
    estacion.textContent = 'Verano';
    document.body.style.backgroundImage = "url('../img/fondo/fondo-granja.jpg')";
  }
  
}



const timePlus = document.getElementById('time-plus');
const fechaHtml = document.getElementById('fecha');

let velocidad = Number(fechaHtml.dataset.velocidad);
let tmp = tiempoDeIA(velocidad);

timePlus.addEventListener('click', ()=> {
  const fecha_nueva = moment(fechaHtml.dataset.fecha);

  if(velocidad === 1000){
    clearInterval(tmp);
    fechaHtml.dataset.velocidad = '10';
    velocidad = Number(fechaHtml.dataset.velocidad);
    tmp = tiempoDeIA(velocidad, fecha_nueva);
    timePlus.textContent = 'Normal';
  }else{
    clearInterval(tmp);
    fechaHtml.dataset.velocidad = '1000';
    velocidad = Number(fechaHtml.dataset.velocidad);
    tmp = tiempoDeIA(velocidad, fecha_nueva);
    timePlus.textContent = 'x100';
  }
});




agenteGranjero(URL, [])
  .then((response) => response.json())
  .then((data) => {
    acciones(data.message);
  });