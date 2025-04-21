import heapq
import numpy as np
def kk_alg(a):
    print(f"Current sequence: {a}")
    a1 = []
    a2 = []
    maxes = heapq.nlargest(2,a)
    max1 = np.int64(maxes[0])
    print(f"Largest element: {max1}")
    max2 = np.int64(maxes[1])
    print(f"Second-largest element: {max2}")
    if(max2 == 0):
        print(f"Residue found: {max1}")
        return max1
    a.remove(max1)
    a1.append(max1)
    a.remove(max2)
    a2.append(max2)
    a.append(np.int64(abs(max1 - max2)))
    a.append(np.int(0))
    return kk_alg(a)

def rep_random(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)
    for _ in range(25000):
        sol2 = np.random.randint(low=1, high=len(a),size=len(a),dtype=np.int64)
        if(kk_alg(sol2) < kk_alg(sol)):
            sol = sol2
    return sol


