$(document).ready(function() {
    function initialize() {
        var mapOptions = {
            center: new google.maps.LatLng(-34.397, 150.644),
zoom: 8
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
   
    var kmlurl="{% static 'kern.kml' %}";
    var precinctLayer = new google.maps.KmlLayer({
        url: kmlurl
    });
    precinctLayer.setMap(map);
    }

    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var fileInput = document.getElementById('fileInput');
        var fileDisplayArea = document.getElementById('fileDisplayArea');
        fileInput.addEventListener('change', function(e) {
            var file = fileInput.files[0];
            var textType = /text.*/;
            var data;

            if (file.type.match(textType)) {
                var reader = new FileReader();

                reader.onload = function(e) {
                    data = reader.result;
                    fileDisplayArea.innerText = data;        
                    data = data.split("\n");
                    for (var i = 1; i < data.length; i++) {
                        var data_line = data[i].split(",");
                        var precinct = data_line[0];
                        var vote_yes = data_line[1];
                        var vote_no = data_line[4];  

                        if (vote_yes && vote_no) {
                            var number = vote_yes - vote_no;
                            if (number < 0) {
                                colorPolygon(ge_obj, precinct, -1);
                            }
                            if (number > 0) {
                                colorPolygon(ge_obj, precinct, 1);
                            }
                            if (number == 0) {
                                colorPolygon(ge_obj, precinct, 0);
                            }
                        }  

                    }             
                } // end of reader onload function
                reader.readAsText(file);   
                ge.getFeatures().appendChild(ge_obj);
                var la = ge.createLookAt('');
                la.set(35.321394, -119.016564, 25, ge.ALTITUDE_RELATIVE_TO_GROUND,
                        0, 0, 40000);
                ge.getView().setAbstractView(la);      
            } else {
                fileDisplayArea.innerText = "File not supported!";
            }
        }); // End of addEventListener
    } else {
        alert('The File APIs are not fully supported by your browser.');
    }     
    
    google.maps.event.addDomListener(window, 'load', initialize);
});
