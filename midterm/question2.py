def find_missing_integer(array):
    i = 0
    if array[0][len(array[0]) - 1] != "0":
        return 0
    for i in range(len(array) - 1):
        temp1 = array[i]
        temp2 = array[i + 1]
        if temp1[len(temp1) - 1] == temp2[len(temp2) - 1]:
            return i + 1


if __name__ == '__main__':
    arr = ["0000", "0001", "0010", "0011", "0101"]
    print("The number is ", find_missing_integer(arr))
