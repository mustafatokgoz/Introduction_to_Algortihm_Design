def quicksort_with_insertion_sort(array, start, end):
    if start < end:
        size = start - end + 1
        if size < 6:
            insertion_sort(array, start, end)
        else:
            pivot = partition(array, start, end)
            quicksort_with_insertion_sort(array, start, pivot - 1)
            quicksort_with_insertion_sort(array, pivot + 1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i = i + 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i + 1]
    array[i + 1] = array[end]
    array[end] = temp
    return i + 1


def insertion_sort(array, start, end):
    for i in range(start + 1, end + 1):
        element = array[i]
        j = i - 1
        while j >= 0 and array[j] > element:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = element


if __name__ == '__main__':
    arr = [4, 3, 456, 7, 2, 8, 5, 4, 89, 4, 5,6,23,66,7]
    quicksort_with_insertion_sort(arr, 0, len(arr) - 1)
    print (arr)
