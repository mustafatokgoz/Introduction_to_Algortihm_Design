
S = [0]*100
def algorithm_question1(arr, size, curpos, length):
    sum = 0
    global S
    if curpos == size:
        for i in range(length):
            sum += S[i]
        if sum == 0:
            for j in range(length):
                print ( S[j], end=" ")
            print()
        return 0
    S[length] = arr[curpos]
    arr.append(algorithm_question1(arr, size, curpos + 1, length + 1) or algorithm_question1(arr, size, curpos + 1, length))
    return arr[size]


if __name__ == '__main__':
    arr = [2, 3, -5, -8, 6, -1]
    algorithm_question1(arr, 6, 0, 0)
