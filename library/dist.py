import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCBomZqjzkNGH8jWT4ULH8R25NuluqhjUY')
loc = gmaps.geolocate()
print(loc)
