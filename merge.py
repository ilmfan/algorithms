def merge(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)



