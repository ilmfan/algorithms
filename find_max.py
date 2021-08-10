def find_max(array):
    max = array[0]
    max_index = 0
    for n in range(1, len(array)):
        if array[n] > max:
            max = array[n]
            max_index = n
    return max_index
