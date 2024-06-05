def potenz (x,y,n):
    pot=1
    while y>0:
        if y%2==0:
            x=(x**2)%n
            y=y//2
        else:
            pot=(pot*x)%n
            y=y-1
    x=pot
    return x

print(potenz(2,228,190))
