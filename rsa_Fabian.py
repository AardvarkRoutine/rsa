print("Berechnung des größten gemeinsamen Teilers")
print("mit einem rekursiven euklidischen Algorithmus")  # Added missing closing parenthesis
zahl_1 = int(input("erste ganze Zahl: "))
zahl_2 = int(input("zweite ganze Zahl: "))

def euklid_rek(wert_1, wert_2):
    if wert_2 == 0:
        return wert_1
    else:
        print("rekursiver Aufruf mit:", str(wert_1), str(wert_2))
        return euklid_rek(wert_2, (wert_1 % wert_2))

print("Der größte gemeinsame Teiler ist " + str(euklid_rek(zahl_1, zahl_2)))

# x**y mod n

def ModPotenzieren(x,y,n):
    
    return x


def verschuesseln((e,n), klartex):
    geheimtext=0
    geheimtext=ModPotenzieren(klartext, e, n)
    return geheimtext

def entschuesseln((d,n), geheimtext):
    klartext=0
    klartext=ModPotenzieren(geheimtext, d, n)
    return klartext

