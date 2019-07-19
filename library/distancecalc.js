  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
  else {
   console.log("nothing");
  }


function showPosition(position) {
  console.log(position)
}

var origin1 = new google.maps.LatLng(55.930385, -3.118425);
