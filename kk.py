import heapq

def kk_alg(a):
    print(f"Current sequence: {a}")
    a1 = []
    a2 = []
    maxes = heapq.nlargest(2,a)
    max1 = maxes[0]
    print(f"Largest element: {max1}")
    max2 = maxes[1]
    print(f"Second-largest element: {max2}")
    if(max2 == 0):
        print(f"Residue found: {max1}")
        return max1
    a.remove(max1)
    a1.append(max1)
    a.remove(max2)
    a2.append(max2)
    a.append(abs(max1 - max2))
    a.append(0)
    return kk_alg(a)

def rep_random(a):
    