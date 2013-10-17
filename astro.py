import sys
import os
import ephem
from datetime import datetime

def loc():
    print "Set your location"
    
    global lat
    lat = raw_input('Lat: ')
    
    global lon
    lon = raw_input('Lon: ')

def choice():
    print "Press 1 to find a star, 2 to find a planet"
    choice = raw_input('> ')
    
    if choice == '1':
        star(raw_input('Star: '))
    
    elif choice == '2':
        const(raw_input('Planet: '))
    
    else:
        print "Try again"
        restart()

def const(planet_name):            # function name and parameters 
    planet_class = getattr(ephem, planet_name)  # sets ephem object class
    date_class = datetime.now()
    planet = planet_class()                     # sets planet variable 
    south_bend = ephem.Observer()               # Creates the Observer object 
    south_bend.lat = lat                # latitude 
    south_bend.lon = lon                   
    south_bend.date = date_class                # sets date parameter
    planet.compute(south_bend)                  # calculates the location data
    print 'Date ', date_class
    print 'RA ', planet.ra
    print 'Dec ', planet.dec
    print 'Alt ', planet.alt
    print 'Az ', planet.az
    
    next = raw_input('Would you like to look up another object?')
    if next.strip() in 'y Y yes Yes YES'.split():
        choice()

def star(star_name):
    star = ephem.star(star_name)
    south_bend = ephem.Observer()
    date_class = datetime.now()
    south_bend.lat = lat
    south_bend.lon = lon
    south_bend.date = date_class
    star.compute(south_bend)
    print "Date ", date_class
    print "Mag ", star.mag
    print "RA ", star.ra
    print "Dec ", star.dec
    
    next = raw_input('Would you like to look up another object?')
    if next.strip() in 'y Y yes Yes YES'.split():
        choice()

if __name__ == '__main__':
    print "Welcome to PySky"
    
    loc()
    choice()
