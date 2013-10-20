function initialize() {
	console.log(1);
  var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
  var mapOptions = {
    zoom: 4,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!'
  });
}

/*var g_map = {
    
    initialize: function(places=[]) {
			console.log("1");
        var mapOptions = {
            zoom: 4,
            center: myLatlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        for(var i=0; i<places.length; i++) {
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(places[i]['lat'], places[i]['lng']);
                map: map,
              //  title: 'Hello World!'
            });
        }
    }
}
*/

google.maps.event.addDomListener(window, 'load', initialize);
