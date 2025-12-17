


def soma_parcial(i, somaTotal, somaParcial, nums, subconjunto):
    n = len(nums)

    #if somaParcial == somaTotal:
        #print(subconjunto)

    if i == n:
        print(subconjunto)
        return
    
    if (somaParcial + nums[i] <= somaTotal):
        subconjunto.append(nums[i])
        soma_parcial(i+1, somaTotal, somaParcial + nums[i], nums, subconjunto)
        soma_parcial(i+1, somaTotal, somaParcial, nums, subconjunto)
    if (somaParcial + nums[i] > somaTotal):
        soma_parcial(i+1, somaTotal, somaParcial, nums, subconjunto)




nums = [1,2,5,6,8]
d = 9
soma_parcial(0,d,0,nums,[])