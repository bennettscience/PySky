import ephem

m = getattr(ephem, (raw_input('Planet: ')))

print ephem.constellation(m(raw_input('yyyy/mm/dd: ')))