#MUSTAFA TOKGOZ 171044077

def algorithm_question3(X, revenue, M, n):
    MaxR = [0 for x in range(M+1)]
    # because there is restriction any 2 ad has to be more than res.
    nextad = 0
    for i in range(1,M+1):
        if (nextad < n):
            if (X[nextad] != i):
                MaxR[i] = MaxR[i-1]
            else:
                if (i <= 4):
                    if (MaxR[i-1] > revenue[nextad]):
                        MaxR[i] = MaxR[i-1]
                    else:
                        MaxR[i] = revenue[nextad]
                else:
                    if ((MaxR[i-5] + revenue[nextad]) > MaxR[i-1]):
                        MaxR[i] = MaxR[i-5] + revenue[nextad]
                    else:
                        MaxR[i] = MaxR[i-1]
                nextad = nextad + 1
        else:
            MaxR[i] = MaxR[i-1]
    return MaxR[M]




if __name__ == "__main__":
        M = 10
        X = [2, 8, 12]
        revenue = [9, 6, 7]
        n = len(X)
        print("M ", M)
        print("Road ",X)
        print("Revenue ",revenue)
        print("Maximum Revenue",algorithm_question3(X,revenue,M, n))
