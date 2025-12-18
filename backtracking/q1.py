#GERAR SUBCONJUNTOS DE UM ARRAY

def subconjunto(itens, i, subset, sub):
    n = len(itens)

    if i == n:
        subset.append(sub[:])
        return

    sub.append(itens[i])
    subconjunto(itens, i+1, subset, sub)
    sub.pop()
    subconjunto(itens, i+1, subset, sub)


nums = [1,2]
subset = []
subconjunto(nums,0,subset,[])
print(subset)