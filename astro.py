import ephem

def const(planet_name, date_string):            # function name and parameters 
    planet_class = getattr(ephem, planet_name)  # sets ephem object class 
    planet = planet_class()                     # sets planet variable 
    south_bend = ephem.Observer()               # Creates the Observer object 
    south_bend.lat = '41.67'                    # latitude 
    south_bend.lon = '-86.26'                   # west is negative
    south_bend.date = date_string               # sets date parameter
    planet.compute(south_bend)                  # calculates the location data
    print ephem.constellation((planet.ra, planet.dec))
    return planet.alt, planet.az

print const(raw_input('Planet: '), getattr(ephem, now()))
