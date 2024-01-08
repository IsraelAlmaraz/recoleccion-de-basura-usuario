var zona1 = window.zona1;
var map = window.map;

const fechaInput = document.getElementById('fecha');


//hacer get para status

console.log(zona1.getPath().getArray());

var marcador;
var coordenadas;

function agregarMarcador(evento) {
    if (marcador) {
        marcador.setMap(null);
    }

    marcador = new google.maps.Marker({
        position: evento.latLng,
        map: map,
        draggable: false
    });

    coordenadas = { lat: marcador.getPosition().lat(), lng: marcador.getPosition().lng() }


    console.log(coordenadas);
}

google.maps.event.addListener(zona1, 'click', agregarMarcador);

fechaInput.addEventListener('change', function () {
    const fechaSeleccionada = fechaInput.value;
    console.log('Fecha seleccionada:', fechaSeleccionada);
    console.log(typeof fechaInput.value)
});


document.getElementById('BotonEnviar').addEventListener('click', function () {

    const fecha = fechaInput.value;

    console.log(fecha);

    //de ser posible añadir selector de fecha, esto permitirá hacer una nueva solicitud, aún con una en curso
    if (coordenadas === undefined) {
        alert('Aún no has especificado un punto de recogida.');
    }

    else if (fecha === "") {
        alert('Aún no has especificado una fecha.');
    }

    else {
        alert('¡Solicitud aprobada!, pasaremos por tu basura el ' + fecha);
        //enviar a la base de datos
        //añadir el ID
        //añadir estatus aprobado


        //LAT, LON, FECHA


        /* fetch('/guardar-datos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(coordenadas),
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Error al enviar datos:', error);
            }); */
    }



});

//botón enviar, al presionar mandar 'coordenadas' a la base de datos