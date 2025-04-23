import heapq
import numpy as np

def kk_alg(a):
    print(f"Current sequence: {a}")
    heapq.heapify(a)
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
    a.append(int(0))
    return kk_alg(a)

def sol_to_seq(a,b):
    seq = np.zeros(shape=len(b))
    for i in range(start=1,stop=len(b)):
        p = b[i]
        seq[p] = seq[p] + a[i]
    return seq

def rep_random(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)
    for _ in range(start=1,stop=25001):
        sol2 = np.random.randint(low=1, high=len(a),size=len(a),dtype=np.int64)
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol

def hill_climbing(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)

    for _ in range(start=1,stop=25001):
        sol2 = sol[:]
        sol[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] = -1 * sol[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] 
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol

#def simul_anneal(a):


example1 = [10,8,7,6,5]


