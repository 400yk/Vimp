$(document).ready(function() {
    var geoXmlDoc;
    var map;
    var info_window = null;
    var precinct_list = [];
    function initialize() {
        $("#map-canvas").html("Loading map...");
        var mapOptions = {
            center: new google.maps.LatLng(35.321394, -119.016564),
zoom: 10
        };
        map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
        var kmlurl = STATIC_URL + "KERN.kml";
        var myParser = new geoXML3.parser({
            map: map,
            afterParse: useTheData
        });
        myParser.parse(kmlurl);
    }

    try {
        google.maps.event.addDomListener(window, 'load', initialize);
    } catch (ReferenceError) { 
        $("#map-canvas").html("Cannot load Google map, please check your internet connection.");
    }

    // Fill in the list of precinct using the default list from database
    $.get('/vm/home_precinct_list/', {precinct_list: null}, function(data) {
        $("#home-precinct-list").html(data);
        $(".btn-detail-class").hide();

        // Once user clicks on any precinct, update map to show it
        $(".individual-precinct").click(function() {
            var name = $(this).attr("precinct-name");
            var coord_lat = $(this).attr("coord-lat");
            var coord_lng = $(this).attr("coord-lng");
            var coord_alt = $(this).attr("coord-alt");
            if (map != null) {
                map.panTo(new google.maps.LatLng(coord_lat, coord_lng));
                map.setZoom(13);

                // Turn on the info window for that placemark
                for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
                    var placemark = geoXmlDoc.placemarks[i];
                    // Color the polygon with name equals to prcinct
                    if (placemark.polygon && placemark.name == name) {
                        // We can just call the click listener we definted before
                        var e = new Object();
                        e.latLng = new google.maps.LatLng(parseFloat(coord_lat),parseFloat(coord_lng + 0.1));
                        google.maps.event.trigger(placemark.polygon, "click", e);
                    }
                }
            }
            // Show the detail button associated with the precinct
            $(".btn-detail-class").hide();
            $("#btn-detail-" + name).show();

        });
            $(".individual-precinct").mouseenter(function() {
                $(".individual-precinct").removeClass('bold');
                $(this).addClass('bold');
            });

            $(".individual-precinct").mouseleave(function() {
                $(".individual-precinct").removeClass('bold');
            });


    });

    function useTheData(doc) {
        geoXmlDoc = doc[0];
        // Remove the markers on the map
        for (var i=0;i<geoXmlDoc.markers.length;i++) {
            geoXmlDoc.markers[i].setVisible(false);
        }
        for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
            var placemark = geoXmlDoc.placemarks[i];
            if (placemark.polygon) {
                placemark.polygon.setOptions({fillOpacity: 0});
                // Remove the default listeners that is on every polygon
                google.maps.event.clearListeners(placemark.polygon, 'click');

            } 
        }
    }

    // Convert numeric value to hexadecimal colors
    function getColor(value) {
        // More votes for republican, show red
        var red = 0;
        var blue = 0;
        var green = 0;
        if (value > 1) {
            var trimmed_value = Math.min(value, 3);
            red = 255;
            blue = Math.round((1 - trimmed_value / 3) * 255);
            green = Math.round((1 - trimmed_value / 3) * 255);
            trimmed_value = null;
        } else if (value == 1) {
            return "#FFFFFF";
        } else if (value < 1) {
            var trimmed_value = 1 / value;
            trimmed_value = Math.min(trimmed_value, 3);
            blue = 255;
            red = Math.round((1 - trimmed_value / 3) * 255);
            green = Math.round((1 - trimmed_value / 3) * 255);
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

    function addOnClickListener(poly, polynum, infoWindowOptions) {
        google.maps.event.addListener(poly, "click", function(e) {
            if (info_window) {
                info_window.close();
            }
            info_window = this.infoWindow;
            info_window.setOptions(infoWindowOptions);
            if (e && e.latLng) {
                info_window.setPosition(e.latLng);
            } else { 
                // This is needed because when we call from another 
                // function there's no position for the mouse
            }
            info_window.open(this.map || this.polylines[0].map);
        });
    }

    function colorPolygon(precinct, color, vote_yes, vote_no, yardsign, undecided) {
        for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
            var placemark = geoXmlDoc.placemarks[i];
            // Color the polygon with name equals to prcinct
            if (placemark.polygon && placemark.name == precinct) {
                var hex_color = getColor(color)
                    var colorOptions = {fillColor: hex_color, fillOpacity: 0.8};
                placemark.polygon.setOptions(colorOptions); 
                // Add information when user clicks on the precinct
                var infoWindowOptions = geoXML3.combineOptions({
                    content: '<div class="geoxml3_infowindow"><h3>' + placemark.name + '</h3><div><ul>' + 
                    '<li>Voted yes: ' + vote_yes + '</li>' +
                    '<li>Voted no: ' + vote_no + '</li>' +
                    '<li>Yardsign: ' + yardsign + '</li>' +
                    '<li>Undecided: ' + undecided + '</li>'  
                    + '</ul></div></div>',
                    pixelOffset: new google.maps.Size(0, 2)
                });
                // Save precinct and then pass it to the list to be shown
                var point_coord = placemark.Point.coordinates[0];
                precinct_list.push({
                    'name': placemark.name,
                    'color': hex_color,
                    'coord_lat': point_coord['lat'],
                    'coord_lng': point_coord['lng'],
                    'coord_alt': point_coord['alt'],
                    'area': google.maps.geometry.spherical.computeArea(placemark.polygon.getPath())
                });
                addOnClickListener(placemark.polygon, i, infoWindowOptions);
            }
        }

    }

    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var fileInput = document.getElementById('fileInput');
        // var fileDisplayArea = document.getElementById('fileDisplayArea');
        fileInput.addEventListener('change', function(e) {
            var file = fileInput.files[0];
            var textType = /text.*/;
            var data;

            if (file.type.match(textType)) {
                var reader = new FileReader();

                reader.onload = function(e) {
                    data = reader.result;
                    // fileDisplayArea.innerText = data;        
                    data = data.split("\n");
                    for (var i = 1; i < data.length; i++) {
                        var data_line = data[i].split(",");
                        var precinct = data_line[0];
                        var vote_yes = data_line[1];
                        var yardsign = data_line[2];
                        var undecided = data_line[4];
                        var vote_no = data_line[3];  

                        if (vote_yes || vote_no) {
                            colorPolygon(precinct, (vote_yes + 0.001) / (vote_no + 0.001), vote_yes, vote_no, yardsign, undecided);
                        }
                    }             
                    // Create the list of placemarks to display on the home page
                    $.get('/vm/home_precinct_list/', {precinct_list: JSON.stringify(precinct_list)}, function(data) {
                        $("#home-precinct-list").html(data);
                        $(".btn-detail-class").hide();

                        // Once user clicks on any precinct, update map to show it
                        $(".individual-precinct").click(function() {
                            var name = $(this).attr("precinct-name");
                            var coord_lat = $(this).attr("coord-lat");
                            var coord_lng = $(this).attr("coord-lng");
                            var coord_alt = $(this).attr("coord-alt");
                            map.panTo(new google.maps.LatLng(coord_lat, coord_lng));
                            map.setZoom(13);

                            // Turn on the info window for that placemark
                            for (var i=0;i<geoXmlDoc.placemarks.length;i++) {
                                var placemark = geoXmlDoc.placemarks[i];
                                // Color the polygon with name equals to prcinct
                                if (placemark.polygon && placemark.name == name) {
                                    // We can just call the click listener we definted before
                                    var e = new Object();
                                    e.latLng = new google.maps.LatLng(parseFloat(coord_lat),parseFloat(coord_lng + 0.1));
                                    google.maps.event.trigger(placemark.polygon, "click", e);
                                }
                            }
                            // Show the detail button associated with the precinct
                            $(".btn-detail-class").hide();
                            $("#btn-detail-" + name).show();

                        });

                        $(".individual-precinct").mouseenter(function() {
                            $(".individual-precinct").removeClass('bold');
                            $(this).addClass('bold');
                        });

                        $(".individual-precinct").mouseleave(function() {
                            $(".individual-precinct").removeClass('bold');
                        });


                    });

                } // end of reader onload function
                reader.readAsText(file);   
            } else {
                // fileDisplayArea.innerText = "File not supported!";
            }
        }); // End of addEventListener
    } else {
        alert('The File APIs are not fully supported by your browser.');
    }     

});
