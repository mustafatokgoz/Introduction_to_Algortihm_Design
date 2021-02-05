import copy


def find_min_index(array):
    min_index = 0
    if array[0] == -1:
        min_index = 1
    for i in range(len(array)):
        if array[i] != -1 and array[i] < array[min_index]:
            min_index = i

    return min_index


def find_max_index(array):
    max_index = 0
    if array[0] == -1:
        max_index = 1
    for i in range(len(array)):
        if array[i] != -1 and array[i] > array[max_index]:
            max_index = i
    return max_index


def clone(a):
    new = copy.deepcopy(a)
    return new


def algorithm(array):
    count_max = 0
    arr2 = clone(array)
    result = [0] * len(array)
    last_result = []

    for i in range(len(array)):
        count_max2 = count_max
        count_max = 0
        if i == 1:
            last_result = result[:]
        for j in range(len(array)):
            min = find_min_index(arr2[j])
            max = find_max_index(arr2[j])
            if max == min:
                count_max += 1
            result[j] = arr2[j][min]
        if i != len(array) - 1 :
            for k in range(len(array)):
                arr2[k][min] = - 1
        if count_max <= count_max2:
            last_result = result[:]
        arr2 = clone(array)
        mini = find_min_index(array[i])
        arr2[i][mini] = -1
        array[i][mini] = -1



    return last_result


if __name__ == '__main__':
    arr = [[2, 11, 13], [1, 11, 7], [3, 11, 20]]
    print(arr)
    print(algorithm(arr))
