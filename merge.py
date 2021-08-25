def merge(a, lb, mid, ub):
    n1 = mid - lb + 1
    n2 = ub - mid
    l, r =[], []
    for w in range(n1 + 1):
        l.append(w)
    for t in range(n2 + 1):
        r.append(t)
    for i in range(n1):
        l[i] = a[lb + i]
    for j in range(n2):
        r[j] = a[mid + j]
    l[n1 + 1] = "stop l"
    r[n2 + 1] = "stop r"
    i = 1
    j = 1





def merge_sort(a, lb, ub):  # lb-lower bound and ub-upper bound
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(a, lb, mid)
        merge_sort(a, (mid + 1), ub)
        merge(a, lb, mid, ub)


# list1 = [15, 5, 24, 8, 1, 3, 16, 10, 20]
# print(merge_sort(list1, 0, 8))
