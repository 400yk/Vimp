$(document).ready(function() {
    var geoXmlDoc;

    function initialize() {
        var mapOptions = {
            center: new google.maps.LatLng(35.321394, -119.016564),
zoom: 10
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
        var kmlurl = "http://127.0.0.1:8000" + STATIC_URL + "kern.kml";
        var myParser = new geoXML3.parser({
            map: map,
            afterParse: useTheData
        });
        myParser.parse(kmlurl);
    }

    google.maps.event.addDomListener(window, 'load', initialize);

    function useTheData(doc) {
        geoXmlDoc = doc[0]
            // Remove the markers on the map
            for (var i=0;i<geoXmlDoc.markers.length;i++) {
                geoXmlDoc.markers[i].setVisible(false);
            }
            for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
               var placemark = geoXmlDoc.placemarks[i];
               if (placemark.polygon) {
                    placemark.polygon.setOptions({fillOpacity: 0});
               } 
            }
    }

    // Convert numeric value to hexadecimal colors
    function getColor(value) {
        // More votes for republican, show red
        var red = 0;
        var blue = 0;
        var green = 0;
        if (value > 0) {
            var trimmed_value = Math.min(value / 0.7, 1);
            red = 255;
            blue = Math.round((1 - trimmed_value) * 255);
            green = Math.round((1 - trimmed_value) * 255);
            trimmed_value = null;
        } else if (value == 0) {
            return "#FFFFFF";
        } else if (value < 0) {
            var trimmed_value = Math.max(value / 0.7, -1);
            blue = 255;
            red = Math.round((1 + trimmed_value) * 255);
            green = Math.round((1 + trimmed_value) * 255);
            trimmed_value = null;
        }
        var second = red % 16;
        var first = (red - second) / 16;
        var fourth = green % 16;
        var third = (green - fourth) / 16;
        var sixth = blue % 16;
        var fifth = (blue - sixth) / 16;
        return ("#" + first.toString(16) + second.toString(16) + third.toString(16) + fourth.toString(16) + fifth.toString(16) + sixth.toString(16));
    }

    function colorPolygon(precinct, color) {
        for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
            var placemark = geoXmlDoc.placemarks[i];
            // Color the polygon with name equals to prcinct
            if (placemark.polygon && placemark.name == precinct) {
                var colorOptions = {fillColor: getColor(color), fillOpacity: 0.8};
                placemark.polygon.setOptions(colorOptions); 
            }
        }
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
                            colorPolygon(precinct, (vote_yes - vote_no) / (vote_yes + vote_no));
                        }
                    }             
                } // end of reader onload function
                reader.readAsText(file);   
            } else {
                fileDisplayArea.innerText = "File not supported!";
            }
        }); // End of addEventListener
    } else {
        alert('The File APIs are not fully supported by your browser.');
    }     

});
