def futurereader(a,b):
    b += -a
    a += b
    b = -b + a
    return a, b
