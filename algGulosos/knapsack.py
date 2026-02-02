#Problema da Mochila Fracionaria

#itens = [(valor,peso)]
def knapsack(itens, W):
    itens = ordenarDecrescente(itens)
    resultado = [0 for i in range(len(itens))]
    i = 0
    peso = 0

    while peso < W and i < len(itens):
        #CASO 1 -> cabe o itens por total
        if itens[i][1] + peso <= W:
            resultado[i] = 1
            peso += itens[i][1]
        else:
            resultado[i] = (W - peso) / itens[i][1]
            peso = W

        i += 1
        
    return resultado

       
 
    



def ordenarDecrescente(itens):
    return sorted(itens, key=lambda item: item[0] / item[1], reverse=True) #valor/peso

result = knapsack([(15,20), (5,30), (10,50), (5,10)], 35)
print(result)