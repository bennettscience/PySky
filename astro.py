import ephem
from datetime import datetime

def const(planet_name):            # function name and parameters 
    planet_class = getattr(ephem, planet_name)  # sets ephem object class
    date_class = datetime.now()
    planet = planet_class()                     # sets planet variable 
    south_bend = ephem.Observer()               # Creates the Observer object 
    south_bend.lat = '41.40'                    # latitude 
    south_bend.lon = '-86.15'                   
    south_bend.date = date_class                # sets date parameter
    planet.compute(south_bend)                  # calculates the location data
    print date_class
    print planet.ra, planet.dec
    print planet.alt, planet.az
    return ephem.constellation((planet.ra, planet.dec))

print const(raw_input('Planet: '))
