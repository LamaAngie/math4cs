def gcd(a,b):
    # make sure a is larger than b
    if a < b:
        a, b = b, a
        return a if b==0 else gcd(b, a%b)