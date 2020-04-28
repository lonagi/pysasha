from math import sqrt as mmmsqrt

def PythagoreanTriplet(n):
    s=set()
    for b in range(n):
        for a in range(1, b):
            c=mmmsqrt( a * a + b * b)
            if c%1==0:
                s.add((a, b, int(c)))
    return s

#PythagoreanTriplet(120)