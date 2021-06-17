from geopy.geocoders import Nominatim

def conv_zip_to_latlong(zip):
    geolocator = Nominatim(user_agent="rehome")
    location = geolocator.geocode({"postalcode":zip})
    lat = round(location.latitude,2)
    long = round(location.longitude,2)
    return {'latitude':lat,'longitude':long}