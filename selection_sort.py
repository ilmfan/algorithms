from find_max import find_max
def selection_sort(array):
    new_array = []
    for n in range(len(array)):
        max_index = find_max(array)
        new_array.append(array.pop(max_index))
    return new_array
