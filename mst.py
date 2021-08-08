from sonni_tup_kupaytuvchilarga_ajratish import stka

def mst(n):  # mukammal sonni topish
    a = 0  # a - [asos] deb nomlangan o'zgaruvchi yaratdim
    d = 1  # d - [daraja] deb nomlangan o'zgaruvchi yaratdim
    k = 1  # k - [ko'paytma] deb nomlangan o'zgaruvchi yaratdim
    g = stka(n)
    b = int((len(stka(n)))/2)
    for i in range(0, b):
        k *= ((g[a])**(g[d] + 1) - 1)/(g[a] - 1)
        a += 2
        d += 2
    if k - n == n:
        return n
    else:
        False