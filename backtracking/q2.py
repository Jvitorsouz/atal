#GERAR SUBCONJUNTOS DE UM TAMANHO K

def subconjunto(itens, i, subset, sub, k):

    if len(sub) == k:
        subset.append(sub[:])
        return
    
    if i == len(itens):
        return
    
    # PODA
    #CASO HAJA POUCOS ELEMENTOS
    if len(sub) + (len(itens) - i) < k:
        return
    
    sub.append(itens[i])
    subconjunto(itens, i+1, subset, sub, k)
    sub.pop()
    subconjunto(itens, i+1, subset, sub, k)


nums = [1,2,3]
k = 2
subset = []
subconjunto(nums,0,subset,[], k)
print(subset)