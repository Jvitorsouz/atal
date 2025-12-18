class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def menorCaminho(node, menorParcial, menor):

    #PODA
    if menorParcial > menor:
        return menor

    #PODA
    if not node.right and not node.left:
        return menorParcial + node.value
    
    if node.right:
        menor = menorCaminho(node.right, menorParcial + node.value, menor)
    if node.left:
        menor = menorCaminho(node.left, menorParcial + node.value, menor)

    return menor

root = Node(10)
root.left = Node(1)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(20)
root.left.right.left = Node(5)
root.left.right.right = Node(7)
root.right.right = Node(3)

menor = float('inf')
menor = menorCaminho(root, 0, menor)
print(menor)
