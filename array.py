
def bubble_sort(array):
    len_arr = len(array)-1
    while len_arr > 0:
        i = 0
        while i+1 <= len_arr:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            i += 1
        len_arr -= 1
    return array


def insert_sort(array):
    for i in range(1, len(array)):
        insertion = array[i]
        j = i-1
        while array[j] > insertion and j >= 0:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = insertion
    return array


def selection_sort(array):
    len_arr = len(array)-1
    for i in range(len_arr):
        curr_min = array[i]
        curr_pos = i
        j = i+1
        while j <= len_arr:
            if array[j] < curr_min:
                curr_min = array[j]
                curr_pos = j
            j += 1
        if curr_pos != i:
            array[i], array[curr_pos] = array[curr_pos], array[i]
    return array


def quick_sort(arr, start=0, end=None):
    if not end:
        end = len(arr) - 1
    if start < end:
        divider = partit(arr, start, end)
        quick_sort(arr, start, divider - 1)
        quick_sort(arr, divider + 1, end)


def partit(arr, start, end):
    pivot = arr[end]
    i = start
    j = end-1
    while i <= j:
        if arr[i] <= pivot:
            i += 1
        else:
            if arr[j] > pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[end] = arr[end], arr[i]
    return i


if __name__ == "__main__":
    print(bubble_sort([7, 5, 4, 3, 2, 1, 0]))
    print(selection_sort([7, 5, 4, 3, 2, 1, 0]))
    print(insert_sort([1, 5, 2, 3, 4, 6, 0]))
    array = [2, 6, 3, 7, 8, 5, 7, 9, 4, 1, 0]
    quick_sort(array)
    print(array)
