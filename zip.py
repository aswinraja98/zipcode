# import module
from geopy.geocoders import Nominatim

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# place input
place = input("enter the place")
location = geolocator.geocode(place)

# traverse the data
data = location.raw
loc_data = data['display_name'].split()
print("Full Location")
print(loc_data)
print("Zip code : ",loc_data[-2])
