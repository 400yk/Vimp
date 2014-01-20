$(document).ready(function() {

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
        
    });

    // Javascript for map initialization
    var geoXmlDoc;
    var map;
    var info_window = null;
    function initialize() {
        var mapOptions = {
            center: new google.maps.LatLng(35.321394, -119.016564),
zoom: 10
        };
        map = new google.maps.Map(document.getElementById("map-canvas-voter"), mapOptions);
    }

    google.maps.event.addDomListener(window, 'load', initialize);

});
