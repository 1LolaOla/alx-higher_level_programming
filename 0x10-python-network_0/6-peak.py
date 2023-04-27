def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0:
            return max(list_of_integers[mid], list_of_integers[mid+1])
        elif mid == n - 1:
            return max(list_of_integers[mid], list_of_integers[mid-1])
        elif list_of_integers[mid] >= list_of_integers[mid - 1] and \
                list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1
