def merge(a, lb, mid, ub):
	n1 = mid - lb + 1
	n2 = ub - mid
	l = []
	r = []
	for w in range(n1 + 1):
		l.append(w)
	for f in range(n2 + 1):
		r.append(f)
	for i in range(n1):
		l[i] = a[lb + i]
	for j in range(n2):
		r[j] = a[mid +1 + j]
	l[n1] = 1000000000000
	r[n2] = 1000000000000
	i = 0
	j = 0
	k = lb
	for k in range(len(a)):
		if l[i] <= r[j]:
			a[k] = l[i]
			i += 1
		else:
			a[k] = r[j]
	return a


def merge_sort(a, lb, ub):
	if lb < ub:
		mid = (lb + ub) // 2
		merge_sort(a, lb, mid)
		merge_sort(a, (mid + 1), ub)
		merge(a, lb, mid, ub)
	
	
	
	
list1 = [3, 7, 2, 1, 6, 4, 8, 5]
result = merge_sort(list1, 0, 7)
print(result)