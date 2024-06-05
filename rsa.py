def euclid(a,b):
    if b == 0:
      return a
    else:
        return euklid_rek(b,(a % b))