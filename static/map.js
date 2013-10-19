var g_map = {
    
    initialize: function(places) {
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
                title: 'Hello World!'
            });
        }
    }
}
