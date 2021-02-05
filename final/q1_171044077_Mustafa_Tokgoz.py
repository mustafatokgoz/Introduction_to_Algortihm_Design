#MUSTAFA TOKGOZ 171044077

def algorithm(str):
    n = len(str)
    if n == 0 :
        return ""
    answer = ""
    dp = [[0 for x in range(n)] for x in range(n)]
    max = 0
    for j in range(n):
        for i in range(j+1):
            check = 0
            if str[i] == str[j]:
                check = 1
            if (j-i) > 2 :
                dp[i][j] = dp[i + 1][j-1] and check
            else:
                dp[i][j] = check
            if dp[i][j] == 1 and (j - i + 1) > max:
                max = j - i + 1
                answer = str[i:j+1]
    return answer

if __name__ == '__main__':
    arr = "MUSTAFA"
    print(arr)
    print("Subarray is " + algorithm(arr))

