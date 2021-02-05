
from math import log2

checklist = [[0 for i in range(100)]
          for j in range(100)]


class Interval:
    def __init__(self, left, right):
        self.L = left
        self.R = right


def fill_the_checklist(arr, n):
    global checklist
    for i in range(n):
        checklist[i][0] = i
    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) - 1 < n:
            if (arr[checklist[i][j - 1]] <
                    arr[checklist[i + (1 << (j - 1))][j - 1]]):
                checklist[i][j] = checklist[i][j - 1]
            else:
                checklist[i][j] = checklist[i +
                                      (1 << (j - 1))][j - 1]
            i = i+ 1
        j = j + 1


def findmin(arr, L, R):
    global checklist
    j = int(log2(R - L + 1))
    if (arr[checklist[L][j]] <=
            arr[checklist[R - (1 << j) + 1][j]]):
        return arr[checklist[L][j]]
    else:
        return arr[checklist[R - (1 << j) + 1][j]]


def findMinimums(arr, n, I, m):

    fill_the_checklist(arr, n)

    for i in range(m):
        L = I[i].L
        R = I[i].R
        print("Minimum of interval [%d, %d] is %d" %
              (L, R, findmin(arr, L, R)))


if __name__ == "__main__":
    A = [2,4,5,3,8,5,9,2]
    n = len(A)
    I = [Interval(0, 3), Interval(3, 5),Interval(5, 7)]
    m = len(I)
    print(A)
    findMinimums(A, n, I, m)
