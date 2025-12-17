def comb(itens, i, subconjunto, subset):
    n = len(itens)

    if i == n and subconjunto:
        soma = 0
        for sub in subconjunto:
            soma ^= sub

        subset.append(soma)


    if (i < n):
        subconjunto.append(itens[i])
        comb(itens, i+1, subconjunto, subset)
        subconjunto.pop(-1)
        comb(itens, i+1, subconjunto, subset)


n = [1,3]
subset = []
comb(n, 0, [], subset)
print(sum(subset))