from rsa import *

n = 3001122295343
e = 65537
d = 2384015708753
oeffentlicherSchluessel = (e, n)
privaterSchluessel = (d, n)

klartext=85
print( "geheimtext=",verschluesseln(oeffentlicherSchluessel, klartext))

print("klartext=", entschluesseln(privaterSchluessel, verschluesseln(oeffentlicherSchluessel, klartext)))
