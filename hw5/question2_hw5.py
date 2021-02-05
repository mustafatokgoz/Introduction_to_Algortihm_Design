def algorithm_question2(arr):
    dp = [None] * len(arr)
    n = len(arr) - 1
    myarr = []
    temp = 0
    for i in range(len(arr[n])):
        dp[i] = arr[n][i]
    for i in range(len(arr) - 2, -1, -1):
        for j in range(len(arr[i])):
            if dp[j] < dp[j+1]:
                temp = dp[j]
            else:
                temp = dp[j + 1]
            dp[j] = arr[i][j] + temp
        if i == len(arr)-2:
            myarr.append(temp)
        myarr.append(dp[i]-temp)
    myarr.reverse()
    print(myarr)
    return dp[0]


if __name__ == '__main__':
    arr = [[2],[5, 4],[1, 4, 7],[8,6,9,6]]
    print(algorithm_question2(arr))
