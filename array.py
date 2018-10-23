
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


def quick_sort(array):
    pass


if __name__ == "__main__":
    print(bubble_sort([7, 5, 4, 3, 2, 1, 0]))
    print(selection_sort([7, 5, 4, 3, 2, 1, 0]))
    print(insert_sort([1, 5, 2, 3, 4, 6, 0]))
