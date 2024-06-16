# x**y mod n
def ModPotenzieren(x, y, n):
    return pow(x, y, n)

def verschluesseln(key, klartext):
    e, n = key
    geheimtext = ModPotenzieren(klartext, e, n)
    return geheimtext

def entschluesseln(key, geheimtext):
    d, n = key
    klartext = ModPotenzieren(geheimtext, d, n)
    return klartext

public_key = (5, 14)  
private_key = (11, 14)  

klartext = 9  
geheimtext = verschluesseln(public_key, klartext)
entschluesselter_text = entschluesseln(private_key, geheimtext)

#print("Klartext:", klartext)
#print("Geheimtext:", geheimtext)
#print("Entschlüsselter Text:", entschluesselter_text)
