#Aplicação de algoritmos gulosos para o problema do troco

def troco(valor):
    c = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.5, 0.1]  # Cédulas disponíveis
    resultado = []
    soma = 0
    i = 0
    while soma != valor and i < len(c):
        if soma + c[i] <= valor:
            soma += c[i]
            resultado.append(c[i])
        else:
            i += 1
        

    return resultado


result = troco(2.89)
print(result)