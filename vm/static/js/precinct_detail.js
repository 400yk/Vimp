$(document).ready(function() {
    var input;

    $('.individual-voter').mouseenter(function() {
        $('.individual-voter').removeClass("voter_highlight");
        $(this).addClass("voter_highlight");
    });

    $(".individual-voter").mouseleave(function() {
        $(this).removeClass("voter_highlight");
    });

    // If click on the voter, load the map info and voting history
    $('.individual-voter').click(function() {
        var address = $(this).attr("voter-address");
        var city = $(this).attr("voter-city");
        var state = $(this).attr("voter-state");
        var zipcode = $(this).attr("voter-zipcode");
        var voter_address_input = document.getElementById("voter-address-input");
        $("#voter-address-input").attr("value", address + ", " + city + ", " + state + ", " + zipcode);

        // Move the map to show the location of the voter
        google.maps.event.trigger(voter_address_input, 'focus');
        google.maps.event.trigger(voter_address_input, 'keydown', {keyCode: 13});
    });

    // Javascript for map initialization
    var geoXmlDoc;
    var map;
    var info_window = null;
    function initialize() {
        var markers = []
        var mapOptions = {
            center: new google.maps.LatLng(35.321394, -119.016564),
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            zoom: 10
        };
        map = new google.maps.Map(document.getElementById("map-canvas-voter"), mapOptions);
        input = /** @type {HTMLInputElement} */(
                document.getElementById('voter-address-input'));

        var searchBox = new google.maps.places.SearchBox(
                /** @type {HTMLInputElement} */(input)); 
        google.maps.event.addListener(searchBox, 'places_changed', function() {
            var places = searchBox.getPlaces();

            for (var i = 0, marker; marker = markers[i]; i++) {
                marker.setMap(null);
            }

            markers = [];
            var bounds = new google.maps.LatLngBounds();
            for (var i = 0, place; place = places[i]; i++) {
                var image = {
                    url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
                };

                var marker = new google.maps.Marker({
                    map: map,
                    icon: image,
                    title: place.name,
                    position: place.geometry.location
                });

                markers.push(marker);

                bounds.extend(place.geometry.location);
            }

            map.fitBounds(bounds);
            map.setZoom(16);
        });
    }

    google.maps.event.addDomListener(window, 'load', initialize);
});
