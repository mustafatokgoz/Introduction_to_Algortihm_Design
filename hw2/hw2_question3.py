

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2

        L = array[:mid]

        R = array[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i = i + 1
            else:
                array[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(L):
            array[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            array[k] = R[j]
            j = j + 1
            k = k + 1


def find_pair(array, desired):
    left = 0
    right = len(array)-1
    while left < right:
        if (array[left] * array[right]) == desired:
            print("{%d,%d}" % (array[left], array[right]))
            left = left + 1
        elif (array[left] * array[right]) < desired:
            left = left + 1
        else:
            right = right - 1


if __name__ == '__main__':
    arr = [1, 2, 3, 6, 5, 4]
    desired_number = 6
    print("Given array is ")
    print(arr)
    mergeSort(arr)
    find_pair(arr, desired_number)

