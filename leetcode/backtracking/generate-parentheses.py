def generate(itens, i, currentString, subset):
    n = len(itens)
    if i == 2*n:
        subset.append(currentString)
        return

    generate(itens, i+1, currentString + "(", subset)
    generate(itens, i+1, currentString + ")", subset)


subset = []
itens = ["(", ")"]
generate(itens, 0, "", subset)
print(subset)