def comb(i, atual, listas, res):
    if i == len(listas):
        res.append("".join(atual[:]))
        return

    for v in listas[i]:
        atual.append(v)
        comb(i + 1, atual, listas, res)
        atual.pop()


    


letters = {"2": ["a", "b", "c"],
           "3": ["d", "e", "f"],
           "4": ["g", "h", "i"],
           "5": ["j", "k", "l"],
           "6": ["m", "n", "o"],
           "7": ["p", "q", "r", "s"],
           "8": ["t", "u", "v"],
           "9": ["w", "x", "y", "z"]}
subset = []
comb(0, [], [letters["2"], letters["3"]], subset)
print(subset)