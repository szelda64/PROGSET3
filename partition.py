import sys
import heapq
import numpy as np
import math

def extractNumbers(file):
    with open(file, 'r') as f:
        return list(map(np.int64, f.read().splitlines()))


#KK ALGORITHM

def kk_alg(a):
    #print(f"Current sequence: {a}")
    a = list(a)
    heapq.heapify(a)
    a1 = []
    a2 = []
    maxes = heapq.nlargest(2,a)
    max1 = np.int64(maxes[0])
    #print(f"Largest element: {max1}")
    max2 = np.int64(maxes[1])
    #print(f"Second-largest element: {max2}")
    if(max2 == 0):
        #print(f"Residue found: {max1}")
        return max1
    a.remove(max1)
    a1.append(max1)
    a.remove(max2)
    a2.append(max2)
    a.append(np.int64(abs(max1 - max2)))
    a.append(int(0))
    return kk_alg(a)

def PP_sol_to_seq(a,b):
    seq = np.zeros(shape=len(b))
    for i in range(1,len(b)):
        p = b[i]
        seq[p] = seq[p] + a[i]
    return seq

def eval_sol(a, b):
    a1 = 0
    a2 = 0
    for i in range(len(b)):
        if b[i] == 1:
            a1 += a[i]
        else:
            a2 += a[i]
    return abs(a1-a2)


"""def PP_sol_to_seq(a,b):
    seq = np.array(a)
    res = 
    for i in range(len(a)):
        seq[b[i]] += a[i]
    return seq"""


#REPEATED RANDOM

def rep_random(a):
    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))

    for _ in np.arange(1, 250001, dtype=np.int64):
        sol2 = np.random.choice([np.int64(-1),np.int64(1)], len(a))
        if eval_sol(a,sol2) < eval_sol(a,sol):
            sol = sol2
    return sol

def PP_rep_random(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)
    for _ in np.arange(1, 250001, dtype=np.int64):
        sol2 = np.random.randint(low=1, high=len(a),size=len(a),dtype=np.int64)
        if(kk_alg(PP_sol_to_seq(a,sol2)) < kk_alg(PP_sol_to_seq(a,sol))):
            sol = sol2
    return sol




#HILL CLIMBING

def hill_climbing(a):
    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))

    for _ in np.arange(1, 250001, dtype=np.int64):
        sol2 = np.array(sol)
        while True:
            i,j=np.random.randint(low=1,high=len(a), size=2, dtype=np.int64)
            if i != j:
                break
        sol2[i] *= -1
        if np.random.random() < 0.5:
            sol2[j] *= -1 
        if eval_sol(a,sol2) < eval_sol(a,sol):
            sol = sol2
    return sol

def PP_hill_climbing(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)

    for _ in np.arange(1, 250001, dtype=np.int64):
        sol2 = np.array(sol)
        while True:
            i,j=np.random.randint(low=1,high=len(a), size=2, dtype=np.int64)
            if sol2[i] != j:
                break
        sol2[i] = j
        if(kk_alg(PP_sol_to_seq(a,sol2)) < kk_alg(PP_sol_to_seq(a,sol))):
            sol = sol2
    return sol




#SIMULATED ANNEALING 

def simul_anneal(a):
    initial_temp=np.int64(10**10)
    cooling_rate=np.int64(0.8)

    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))
    sol3 = sol
    for t in np.arange(1, 25001, dtype=np.int64):
        temp = initial_temp * (cooling_rate**(math.floor(t / 300)))

        current_Cost = eval_sol(a,sol)

        sol2 = np.array(sol)
        while True:
            i,j=np.random.randint(low=1,high=len(a), size=2, dtype=np.int64)
            if i != j:
                break
        sol2[i] *= -1
        if np.random.random() < 0.5:
            sol2[j] *= -1 
        
        neighbor_Cost = eval_sol(a,sol2)
        # if neighbor solution is better
        deltaE =  neighbor_Cost - current_Cost
        if temp != np.int64(0):
            prob = np.int64(np.e) **((-deltaE)/temp)
        else:
            prob = np.int64(0)
        
        #if solution is better or if probability says yes to the dress
        if deltaE > 0 or prob > temp: 
            sol = sol2
        if current_Cost < eval_sol(a,sol3):
            sol3 = sol
    return sol3         


def PP_simul_anneal(a):
    initial_temp=np.int64(10**10)
    cooling_rate=np.int64(0.8)

    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)
    sol3 = sol
    for t in np.arange(1, 25001, dtype=np.int64):
        temp = initial_temp * (cooling_rate**(math.floor(t / 300)))

        current_Cost = kk_alg(PP_sol_to_seq(a,sol))

        sol2 = np.array(sol)
        while True:
            i,j=np.random.randint(low=1,high=len(a), size=2, dtype=np.int64)
            if sol[i] != j:
                break
        sol2[i] = j
        neighbor_Cost = kk_alg(PP_sol_to_seq(a,sol2))

        deltaE =  neighbor_Cost - current_Cost
        if temp != np.int64(0): 
            prob = np.int64(np.e) **((-deltaE)/temp)
        else:
            prob = np.int64(0)

        #if solution is better or if probability says yes to the dress
        if deltaE > 0 or prob > temp: 
            sol = sol2
        if current_Cost < eval_sol(a,sol3):
            sol3 = sol

    return sol3


example1 = [10,8,7,6,5]
example1SOL = [1,2,2,4,5]


"""flag = int(sys.argv[1])
algorithm = int(sys.argv[2])
file = sys.argv[3]
a = extractNumbers(file)

if algorithm == 0:
    print(kk_alg(a))
elif algorithm == 1:
    print(eval_sol(a,rep_random(a)))
elif algorithm == 2:
    print(eval_sol(a,hill_climbing(a)))
elif algorithm == 3:
    print(eval_sol(a,simul_anneal(a)))
elif algorithm == 11:
    print(kk_alg(PP_sol_to_seq(a,PP_rep_random(a))))
elif algorithm == 12:
    print(kk_alg(PP_sol_to_seq(a,PP_hill_climbing(a))))
elif algorithm == 13:
    print(kk_alg(PP_sol_to_seq(a,PP_simul_anneal(a))))"""