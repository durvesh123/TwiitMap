var map = L.map('map',{
    center: [5,28],
    zoom:3,
    minZoom:2,
    maxZoom: 18
});

L.tileLayer('http://{s}.tiles.mapbox.com/v3/ianmule.bg2v5cdi/{z}/{x}/{y}.png',{attribution:"Mapbox"})
.addTo(map);

for ( var i=0; i < markers.length; ++i )
{
   L.marker( [markers[i].lat, markers[i].lng] )
      .bindPopup( '<a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a>' )
      .addTo( map );
}
