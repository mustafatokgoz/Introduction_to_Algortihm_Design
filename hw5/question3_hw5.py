
def algorithm_question3(W, n, v, w):
    arr = [0]*(W+1)

    for i in range(W + 1):
        for j in range(n):
            if (w[j] <= i):
                if arr[i] < arr[i - w[j]] + v[j]:
                    arr[i] = arr[i - w[j]] + v[j]

    return arr[W]


if __name__ == '__main__':
    W = 9
    v = [10, 4, 3]
    w = [5, 4, 2]
    n = len(v)
    print(algorithm_question3(W, n, v, w))
