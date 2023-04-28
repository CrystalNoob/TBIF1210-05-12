def random(X0, init_range, end_range):
    a = 11*47*541*911 + 1
    b = 100
    m = 48**5-1
    Xn = (a * X0 + b)%m
    return Xn%(end_range-init_range+1) + init_range 