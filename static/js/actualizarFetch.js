const mapa = window.initMap();

var icon = {
    url: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Icon-mode-bus-default.svg/2048px-Icon-mode-bus-default.svg.png",
    size: new google.maps.Size(50, 50),
    scaledSize: new google.maps.Size(25, 25) // Tamaño en pantalla
};

function actualizar(lista) {

    console.log("dentro 1: ", lista);

    const markers = lista.map((pos) => {
        let latitud = pos.lat;
        let longitud = pos.lon;
        const mark = new google.maps.Marker({
            map: mapa,
            position: { lat: latitud, lng: longitud },
            icon: icon,

        });

        return mark;
    });

}

fetch("http://192.168.177.163:5000/posiciones")
    .then((respuesta) => {
        if (!respuesta.ok) {
            throw new Error(`Error en la solicitud: ${respuesta.status}`);
        }
        return respuesta.json();
    })
    .then((lista) => {
        // Cualquier lógica dependiente de la respuesta va aquí
        console.log('Datos obtenidos:', lista);
        actualizar(lista);
    })
    .catch((error) => {
        console.error('Error:', error.message);
    });
