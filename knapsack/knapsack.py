

MAXVALUE = 0
BESTSOLUTION = []
C = 16
X = [0,0,0,0]
W = [15, 5, 10, 5]
V = [20, 30, 50, 10]


def backtrack(i, currentWeight, currentValue, X):
    n = len(X)
    global BESTSOLUTION
    global MAXVALUE
    if i >= n:
        if currentValue > MAXVALUE:
            MAXVALUE = currentValue
            #Copia do array
            BESTSOLUTION = X[:]
    else:
        if currentWeight + W[i] <= C:
            X[i] = 1
            backtrack(i+1, currentWeight + W[i], currentValue + V[i], X)
        X[i] = 0
        backtrack(i+1, currentWeight, currentValue, X)

backtrack(0,0,0,X)
print(BESTSOLUTION)
print(MAXVALUE)


