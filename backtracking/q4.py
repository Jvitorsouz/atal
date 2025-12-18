def menorCaminho(node, menorParcial, menor):
    if not node.right and not node.left:
        if menorParcial + node.value < menor:
            menor = menorParcial + node.value
        return menor
    

    if menorParcial + node.value < menor:
        if node.right:
            menor = menorCaminho(node.right, menorParcial + node.value, menor)
        if node.left:
            menor = menorCaminho(node.left, menorParcial + node.value, menor)

    return menor