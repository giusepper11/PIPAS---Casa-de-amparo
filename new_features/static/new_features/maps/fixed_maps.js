/**
 * Boilerplate map initialization code starts below:
 */
function addMarkersToMap(map) {
    var marcador = new H.map.Marker({lng:-46.620016 , lat: -23.501195});
    map.addObject(marcador);

}

//Step 1: initialize communication with the platform
var platform = new H.service.Platform({
    app_id: 'AIh2ilqYIkz06xHw5CUu',
    app_code: '2x5wK3xJnFXC8u7mpHFZow',
    // useHTTPS: true
});
var pixelRatio = window.devicePixelRatio || 1;
var defaultLayers = platform.createDefaultLayers({
    tileSize: pixelRatio === 1 ? 256 : 512,
    ppi: pixelRatio === 1 ? undefined : 320
});

//Step 2: initialize a map - this map is centered over Europe
var map = new H.Map(document.getElementById('map'),
    defaultLayers.normal.map, {
        center: {lng:-46.620016 , lat: -23.501195},
        zoom: 16,
        pixelRatio: pixelRatio
    });


//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);

// Now use the map as required...
addMarkersToMap(map);