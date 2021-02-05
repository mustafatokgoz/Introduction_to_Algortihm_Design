def quicksort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot - 1)
        quicksort(array, pivot + 1, end)


count = 0
count2 = 0


def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            global count
            count = count + 1
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
            global count2
            count2 = count2 + 1
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = element


if __name__ == '__main__':
    arr = [4, 3, 456, 7, 2, 8, 5, 4, 89, 4]
    arr2 = [4, 3, 456, 7, 2, 8, 5, 4, 89, 4]
    insertion_sort(arr, 0, len(arr) - 1)
    quicksort(arr2, 0, len(arr) - 1)
    print ("Number of swap operation of quicksort is")
    print (count)
    print (arr2)
    print ("Number of swap operation of insertion sort is")

    print (count2)
    print (arr)
