import ephem
from datetime import datetime
    
def star(star_name):
    star = ephem.star(star_name)
    south_bend = ephem.Observer()
    date_class = datetime.now()
    south_bend.lat = '41.15'
    south_bend.lon = '-86.26'
    south_bend.date = date_class
    star.compute(south_bend)
    print date_class
    print "Mag ", star.mag
    print "RA ", star.ra
    print "Dec ", star.dec


def const(planet_name):            # function name and parameters 
    planet_class = getattr(ephem, planet_name)  # sets ephem object class
    date_class = datetime.now()
    planet = planet_class()                     # sets planet variable 
    south_bend = ephem.Observer()               # Creates the Observer object 
    south_bend.lat = '41.40'                    # latitude 
    south_bend.lon = '-86.15'                   
    south_bend.date = date_class                # sets date parameter
    planet.compute(south_bend)                  # calculates the location data
    print 'Date ', date_class
    print 'RA ', planet.ra
    print 'Dec ', planet.dec
    print 'Alt ', planet.alt
    print 'Az ', planet.az
    return ephem.constellation((planet.ra, planet.dec))

print "Press 1 to find a star, 2 to find a planet"

choice = raw_input('> ')

if choice == '1':
    star(raw_input('Star: '))
    
else:
    const(raw_input('Planet: '))