	var map;
	var positions = [];
	var markers = [];


	//Inicializa el mapa
	function initMap() {

		map = new google.maps.Map(document.getElementById('map'), {
		  zoom: 8,
		  center: {lat: 5.547870, lng: -73.350298}, 
		});

		setLayer();
		//polylinesMap();
		geocodeAddress();
	}

	//Dibuja el mapa de Boyaca
	function setLayer(){
		var ctaLayer = new google.maps.KmlLayer({
		  url: 'https://www.dropbox.com/s/4b7pqut55cj5u4t/Border.kml?dl=1',
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
	function geocodeAddress() {


	  	for (var i in projects) {

	  		address = projects[i].address.concat(' ',projects[i].municipality,' ',projects[i].department,' Colombia');
	  		console.log('Proyecto '+i+' : '+address);
			
			//2.1. recorrer la lista de direcciones

			var geocoder = new google.maps.Geocoder();
			geocoder.geocode({'address': address}, function(results, status){
			
				if (status === google.maps.GeocoderStatus.OK) {

					lat = results[0].geometry.location.lat();
					lng = results[0].geometry.location.lng();
					
					console.log('Adentro: Las coordenadas son: '+lng+' , '+lat);
						
						
					setPosition(lat, lng, function(callback){
						//console.log('Se guardo '+callback)
					});
						

				} else {
				  //alert('No se ha podido ubicar algunos puntos en el mapa: ' + status);
				}
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

		var contentString = getContentString(i);

		setMarkers(positions[i], projects[i].name, contentString);

		if(positions.length == projects.length)
			setMarkerCluster();

		//return callback('las coordenadas '+positions[i].lng+' , '+positions[i].lat);
	}


	//Función retorna la descripción
	function getContentString(i){
		
	var contentString =
		'<div id="iw-container">' +
			'<div class="iw-title">'+projects[i].name+'</div>' +
				'<div class="iw-content">' +
					'<div class="iw-subTitle">Descripción</div>' +
					'<img src="http://maps.marnoto.com/en/5wayscustomizeinfowindow/images/vistalegre.jpg" alt="Porcelain Factory of Vista Alegre" height="115" width="83">' +
					'<p>Founded in 1824, the Porcelain Factory of Vista Alegre was the first industrial unit dedicated to porcelain production in Portugal. For the foundation and success of this risky industrial development was crucial the spirit of persistence of its founder, José Ferreira Pinto Basto. Leading figure in Portuguese society of the nineteenth century farm owner, daring dealer, wisely incorporated the liberal ideas of the century, having become "the first example of free enterprise" in Portugal.</p>' +
					'<div class="iw-subTitle">Horarios</div>' +
					'<p>'+projects[i].address+'<br> '+projects[i].municipality+' - '+projects[i].department+'<br>'+
					'<br>Phone. +351 234 320 600<br>e-mail: geral@vaa.pt<br>www: www.myvistaalegre.com</p>'+
			'</div>' +
			'<div class="iw-bottom-gradient"></div>' +
		'</div>';

		return contentString;
	}


	//Función encargada de realizar varios marcadores.
	function setMarkers(position, title, contentString){

		var marker = new google.maps.Marker({
	      position: position,
	      map: map,
	      icon:'/static/assets/img/marker_map_indeportes.png',
	      title: title
	    });

	    var i = marker.length;

	    (function(i, marker) {

	    	var infowindow = new google.maps.InfoWindow({
				content: contentString,
				maxWidth: 350
			});

		 
		    google.maps.event.addListener(marker,'click',function() {	
		    	//$('.gm-style-iw').remove();
		        infowindow.open(map, marker);
		    });

			google.maps.event.addListener(map, 'click', function() {
				infowindow.close();
			});

			google.maps.event.addListener(infowindow, 'domready', function() {


			    var iwOuter = $('.gm-style-iw');

			    /* Since this div is in a position prior to .gm-div style-iw.
			     * We use jQuery and create a iwBackground variable,
			     * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
				    */
			    var iwBackground = iwOuter.prev();

			    iwBackground.children(':nth-child(2)').css({'display' : 'none'}); // Removes background shadow DIV
			    iwBackground.children(':nth-child(4)').css({'display' : 'none'}); // Removes white background DIV
			    iwOuter.parent().parent().css({left: '115px'}); // Moves the infowindow 115px to the right.
			    iwBackground.children(':nth-child(1)').attr('style', function(i,s){ return s + 'left: 76px !important;'}); // Moves the shadow of the arrow 76px to the left margin.
			    iwBackground.children(':nth-child(3)').attr('style', function(i,s){ return s + 'left: 76px !important;'}); // Moves the arrow 76px to the left margin.
			    iwBackground.children(':nth-child(3)').find('div').children().css({'box-shadow': 'rgba(72, 181, 233, 0.6) 0px 1px 6px', 'z-index' : '1'}); // Changes the desired tail shadow color.
			    var iwCloseBtn = iwOuter.next(); // Reference to the div that groups the close button elements.
			    iwCloseBtn.css({opacity: '1', right: '38px', top: '3px', border: '7px solid #77DD77', 'border-radius': '13px', 'box-shadow': '0 0 5px #77DD77'}); // Apply the desired effect to the close button

			    // If the content of infowindow not exceed the set maximum height, then the gradient is removed.
			    if($('.iw-content').height() < 140){
			      $('.iw-bottom-gradient').css({display: 'none'});
			    }

			    // The API automatically applies 0.7 opacity to the button after the mouseout event. This function reverses this event to the desired value.
			    iwCloseBtn.mouseout(function(){
			      $(this).css({opacity: '1'});
			    });

			});
		
			//google.maps.event.addDomListener(window, 'load', initialize);
	    
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