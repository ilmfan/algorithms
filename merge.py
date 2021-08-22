def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    l = a[:(n1 + 1)]
    r = a[:(n2 + 1)]
    for i in range(0, (n1 + 1)):
        l[i] = a[(p + i - 1)]
    for j in range(0, (n2 + 1)):
        r[j] = a[(q + j)]
    l[n1 + 1] =
