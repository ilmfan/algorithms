def linear_search(given_array, item):
    for i in range(len(given_array)):
        if given_array[i] == item:
            return i
    return None

