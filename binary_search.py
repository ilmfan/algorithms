def binary_search(given_list, item):
    low = 0
    high = len(given_list)-1
    while low <= high:
        mid = (low + high)//2
        guess = given_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
