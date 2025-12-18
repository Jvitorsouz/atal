#PARENTES VALIDOS

def parenteses(left, right, currentString, subset, k):

    if len(currentString) == 2*k:
        subset.append(currentString)
        return

    if left < k :
        parenteses(left+1, right, currentString+"(", subset, k)
    if right < left:
        parenteses(left, right+1, currentString+")", subset, k)


subset = []
k = 3
parenteses(0,0,"",subset,k)
print(subset)