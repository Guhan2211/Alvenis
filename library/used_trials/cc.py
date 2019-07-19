import googlemaps
from datetime import datetime
import geocoder
gmaps = googlemaps.Client(key='AIzaSyCBomZqjzkNGH8jWT4ULH8R25NuluqhjUY')
fradd=(13.056062, 81.046547)
reverse =gmaps.reverse_geocode(fradd)
#reverse = gmaps.reverse_geocode((38.887563, -77.019929))
li=reverse
print(li)

