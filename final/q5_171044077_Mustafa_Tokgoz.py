#Mustafa Tokgoz 171044077

def InvCount(list, n):
    temp = [0 for x in range(n + 1)]
    return InvCount2(list, temp, 0, n - 1)


def InvCount2(list, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2

        count = count + InvCount2(list, temp, left, mid)

        count = count + InvCount2(list, temp, mid + 1, right)

        count = count + InvCount3(list, temp, left, mid, right)
    return count


def InvCount3(list, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:

        if list[i] <= 2 * list[j]:
            temp[k] = list[i]
            k = k + 1
            i = i + 1
        else:
            # There is inversion if and only if list[i] > list[j]
            temp[k] = list[j]
            count = count + (mid - i + 1)
            k = k + 1
            j = j + 1

    while i <= mid:
        temp[k] = list[i]
        k = k + 1
        i = i + 1

    while j <= right:
        temp[k] = list[j]
        k = k + 1
        j = j + 1

    for m in range(left, right + 1):
        list[m] = temp[m]

    return count


if __name__ == "__main__":
    list = [1,30,6,5]
    n = len(list)
    print(list)
    result = InvCount(list, n)
    print("Total number of inversions is ", result)
    print(list)
