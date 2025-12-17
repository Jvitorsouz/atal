
def somaSub(itens, i, somaParcial, restante, soma, subconjuto):
    n = len(itens)
    if somaParcial == soma:
        print(subconjuto)
    elif (i<n and promissor(itens[i], somaParcial, restante, soma)):
        subconjuto.append(itens[i])
        somaSub(itens, i+1, somaParcial+itens[i], restante-itens[i], soma, subconjuto)
        subconjuto.pop(-1)
        somaSub(itens, i+1, somaParcial, restante, soma, subconjuto)



def promissor(elemento, somaParcial, restante, soma):
    return (somaParcial + restante >= soma) and (somaParcial + elemento <= soma)


nums = [1,2,5,6,8]
d = 9
somaSub(nums, 0, 0, sum(nums), d, [])