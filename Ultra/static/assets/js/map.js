	var map;
	var positions = [];
	var markers = [];


	//Inicializa el mapa
	function initMap() {

		map = new google.maps.Map(document.getElementById('map'), {
		  zoom: 6,
		  center: {lat: 5.547870, lng: -73.350298}, 
		});

		setLayer();
		//polylinesMap();
		setPoints();
	}

	//Dibuja el mapa de Boyaca
	function setLayer(){
		var ctaLayer = new google.maps.KmlLayer({
		  url: 'https://www.dropbox.com/s/c5tqhjvyd7ktblp/poly.kml?dl=1',
		  map: map
		});
	}

	//1. Dibuja el crockis en el mapa de Boyaca
	function polylinesMap(){

		var flightPath = new google.maps.Polyline({
		    path: silhouetteBoyacaMap,
		    geodesic: true,
		    strokeColor: '#097138',
		    strokeOpacity: 1.0,
		    strokeWeight: 5
		});

		flightPath.setMap(map);
	}


	//2. Convierte las direcciones en coordenadas
	function setPoints() {

	  	for (var i in projects) {

	  		address = projects[i].address.concat(' ',projects[i].municipality,' ',projects[i].department,' Colombia');
	  		console.log('Proyecto '+i+' : '+address);


			setPosition(projects[i].lat, projects[i].lon, function(callback){
				//console.log('Se guardo '+callback)
			});
		}
	}


	//Funcion encargada de guardar y marcar las posiciones de las ubicaciones en el mapa
	function setPosition(lat, lng, callback){
		positions.push(
			position = {
				lat: lat,
				lng: lng 
			}
		);

		var i = positions.length -1;

		setMarkers(positions[i], projects[i].name, projects[i]);

		if(positions.length == projects.length)
			setMarkerCluster();

		//return callback('las coordenadas '+positions[i].lng+' , '+positions[i].lat);
	}


	//Función encargada de realizar varios marcadores.
	function setMarkers(position, title, data){

		var marker = new google.maps.Marker({
	      position: position,
	      map: map,
	      icon:'/static/assets/img/marker_map_indeportes.png',
	      title: title
	    });

	    var i = marker.length;

	    (function(i, marker) {
		    google.maps.event.addListener(marker,'click',function() {	
		    	$('#myModal').modal('show');
				$("#markerTitle").html(data.name);
				$("#markerProg").html(data.program);
				$("#markerSub").html(data.subprogram);
				$("#markerAddr").html(data.address);
				$("#markerNeigh").html(data.neighborhood);
				$("#markerVeedor").html(data.veedor);
		    });
	    
	    })(i, marker);

	    markers.push(marker);	    
	}


	//Realiza las agrupaciones de marcadores
	function setMarkerCluster(){

		console.log('Contamos con '+markers.length);

		var markerCluster = new MarkerClusterer(
			map, 
			markers,
		  	{imagePath:'/static/assets/img/m'}
		);
	}