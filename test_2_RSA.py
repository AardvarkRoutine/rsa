from rsa import *

n = 3001122295343
print(primfaktoren(n))
e = 65537
m=(primfaktoren(n)[0]-1)*(primfaktoren(n)[1]-1)
print(m)
d=multInv(e,m)

oeffentlicherSchluessel = (e, n)
privaterSchluessel = (d, n)

klartext=65
print( "geheimtext=",verschluesseln(oeffentlicherSchluessel, klartext))

print("klartext=", entschluesseln(privaterSchluessel, verschluesseln(oeffentlicherSchluessel, klartext)))