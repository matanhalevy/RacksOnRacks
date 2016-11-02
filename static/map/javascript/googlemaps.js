    var myLatLngGlobal;
    var map;


function initMap(){



    var self = {

        // starts all the processes
        //function placeRackMarkers(locations, map) {
        initialize: function () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    var myLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                    myLatLngGlobal = myLatLng;
                    console.log(myLatLng);



                    var zoom = 14;
                    //var latlng = new google.maps.LatLng(lat, lng);
                    //myLatLngGlobal = latlng;
                    var options = {
                        zoom: zoom,
                        center: myLatLngGlobal
                        //mapTypeId:
                    };
                    map = new google.maps.Map(document.getElementById("map_canvas"), options);
                    var bikeLayer = new google.maps.BicyclingLayer();
                    bikeLayer.setMap(map);
                    mapGlobal = map;

                    self.displayRacks();

                    var icon = {
                        url: 'http://i.imgur.com/aZw9X52.png', //url
                        scaledSize: new google.maps.Size(90, 90), //size
                        origin: new google.maps.Point(0, 0), //origin
                        anchor: new google.maps.Point(50, 50) //anchor
                    };

                    var marker = new google.maps.Marker({
                        position: myLatLngGlobal,
                        map: map,
                        title: 'Hello World!',
                        draggable: false,
                        icon: icon,
                        animation: google.maps.Animation.DROP

                    });
                    var myinfowindow = new google.maps.InfoWindow({
                        content: '<p><b>' + 'You are here babe <3' + '</b>'
                    });

                    marker.addListener('click', function () {
                        myinfowindow.open(map, marker);
                    });

                    // self.attachHandlers();

                    //add all the intialiazing functions (self.(....)

                }, function () {
                    handleLocationError(true, infoWindow, map.getCenter());
                });
            } else {
                // Browser doesn't support Geolocation
                handleLocationError(false, infoWindow, map.getCenter());
            }},

        //Event handlers attached
        /*  attachHandlers: function () {
         $("#filterDistance").click(function () {
         filterDistance = "#filterDistance";
         });
         console.log("filterDistance = " + self.filterDistance);
         },

         /*
         var filterDistance1 = document.getElementById("filters").value; //put outside of self var if this doesnt work
         console.log("filterDistance =" + filterDistance1);

         filterDistance = filterDistance1;
         */



        displayRacks: function () {
            var locations;


            var e = document.getElementById("filters");
            var filterDistance = e.options[e.selectedIndex].value;
            console.log("testing "+ filterDistance);
            if (filterDistance == "Fave") {
                $.get('/racks/fave_list/', {}, function (data) {
                    faves = data['faves'];

                    for (var i = 0; i < faves.length; i++){
                        if (faves[i][0] == user){
                            addFaveMarker(i, faves);
                        }
                    }

                });

            }
            else $.get('/racks/map_locations/', {}, function (data) {
                locations = data['racks'];
                filteredRacks = self.filterRacks(filterDistance,locations,myLatLngGlobal);
                self.placeRackMarkers(filteredRacks, map);
            });
        },



        filterRacks:function(filterDistance,racks, markerLatLng) {
            console.log("got to filterRacks");
            var filteredRacks = [];
            if (filterDistance == "16") {
                for (var i = 0; i < racks.length; i++) {
                    if (racks[i][4] != "")
                        filteredRacks.push(racks[i])
                }
            }
            for (var k = 0; k < racks.length; k++) {
                if (self.checkDistance(racks[k], markerLatLng) <= filterDistance) {

                    filteredRacks.push(racks[k]);
                }
            }
            filteredRacksGlobal = filteredRacks;
            console.log(filteredRacks[0]);
            return filteredRacks;},

        placeRackMarkers:function (locations, map) {
            var i;
            for (i = 0; i < locations.length; i++) {
                self.addMarker(i, locations);
            }
        },

        addMarker:function(i, locations) {
            var address = locations[i][0]
            var number = locations[i][3]
            var lat = locations[i][1]
            var lon = locations[i][2]
            var content = '</div>' +
                '<p><b>' + locations[i][0] + '</b>' +
                '<p>It is: ' + '<b>' + Math.round(self.checkDistance(locations[i], myLatLngGlobal)) + 'm' + '</b>' + " away" +
                '<p>Racks: ' + '<b>' + locations[i][3] + '</b>' +
                      '<p>' + '<button onclick="addToFavorites(\'' + address + '\', \'' + number + '\', \'' + lat + '\', \'' + lon + '\')">Favorite</button>' +
                            '<button onclick="addUsed(\'' + address + '\', \'' + number + '\')">Used</button>' + '</b>'
                '</div>';



            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                info: infowindow = new google.maps.InfoWindow({
                    content: content
                }),
                icon: 'http://i.imgur.com/yulaE9p.png',
                map: map
            });

            google.maps.event.addListener(marker, 'click', function () {
                marker.info.open(map, marker);
            });
        },

        checkDistance:function(rack){
            var rackLatLng = new google.maps.LatLng(rack[1], rack[2]);
            return (google.maps.geometry.spherical.computeDistanceBetween(rackLatLng, myLatLngGlobal));
        }
    };

    return self;


}
             function addToFavorites(address, number, l, lon){
        alert("Added to favorites!");
        var abc = user;
                 console.log(abc);
        displayUsers();
                 $.ajax({
        url:'/racks/fave/',
        type: "POST",
        data: {address: address, number: number, lat:l, lon:lon, u:abc,
            csrfmiddlewaretoken:'{{ csrf_token }}'
        },

        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){
        alert("error doing something");
    }
});
        var Latlng = new google.maps.LatLng(parseFloat(l),parseFloat(lon));
        var marker = new google.maps.Marker({
            position: Latlng,
            map: map,
            title: 'Hello World!',
            draggable: false,
            icon: 'http://i.imgur.com/W03Cv2m.png',
            animation: google.maps.Animation.DROP,
            zIndex: google.maps.Marker.MAX_ZINDEX + 1

                    });

    }

       function addUsed(add, num){
            alert("Added to used!");
           var abc = user;
           console.log("Testing+ "+abc);
            $.ajax({

        url:'/racks/used/',
        type: "POST",
        data: {address: add, number: num, u:abc,
            csrfmiddlewaretoken:'{{ csrf_token }}'
        },
        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){
        alert("error doing something");
    }
});
    }

function displayUsers() {
        var users;
        var i;
        var name;
        $.get('/racks/user_list/', {}, function (data) {
            users = data['users'];
            for (i = 0; i < users.length; i++){
                name = users[i][0];
                console.log(name);
            }
        })};

    function addFaveMarker(i, locations) {
            var address = locations[i][1];
            var number = locations[i][2];
            var lat = locations[i][2];
            var lon = locations[i][3];
            var content = '</div>' +
                '<p><b>' + locations[i][1] + '</b>' +
                '<p>Racks: ' + '<b>' + locations[i][4] + '</b>';
                '</div>';



            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][2], locations[i][3]),
                info: infowindow = new google.maps.InfoWindow({
                    content: content
                }),
                icon: 'http://i.imgur.com/W03Cv2m.png',
                map: map
            });

            google.maps.event.addListener(marker, 'click', function () {
                marker.info.open(map, marker);
            });
        }

$(document).ready(function () {
    var googleMap = initMap();
    googleMap.initialize();

    startThis();
});

function rerun(){
    var googleMap = initMap();
    googleMap.initialize();
}

    function goToFavourites(){
        window.location.href= "fave/?user="+user;

    }
