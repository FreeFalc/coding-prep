
def bubble_sort(arr):
    len_arr = len(arr) - 1
    while len_arr > 0:
        i = 0
        while i+1 <= len_arr:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        len_arr -= 1
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        insertion = arr[i]
        j = i-1
        while arr[j] > insertion and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = insertion
    return arr


def selection_sort(arr):
    len_arr = len(arr) - 1
    for i in range(len_arr):
        curr_min = arr[i]
        curr_pos = i
        j = i+1
        while j <= len_arr:
            if arr[j] < curr_min:
                curr_min = arr[j]
                curr_pos = j
            j += 1
        if curr_pos != i:
            arr[i], arr[curr_pos] = arr[curr_pos], arr[i]
    return arr


def quick_sort(arr, start=0, end=None):
    if not end:
        end = len(arr) - 1
    if start < end:
        divider = partitioning(arr, start, end)
        quick_sort(arr, start, divider - 1)
        quick_sort(arr, divider + 1, end)


def partitioning(arr, start, end):
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
