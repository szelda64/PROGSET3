import sys
import heapq
import numpy as np

def extractNumbers(file):
    with open(file, 'r') as f:
        return f.read().splitlines()


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

# def sol_to_seq(a,b):
#     seq = np.zeros(shape=len(b))
#     for i in range(1,len(b)):
#         p = b[i]
#         seq[p] = seq[p] + a[i]
#     return seq

def sol_to_seq(a,b):
    seq = a[:]
    for i in range(len(b)):
        for j in range(len(a)):
            if i < j:
                if b[i] == b[j]:
                    seq[i] += seq[j]
                    seq[j] = 0
    return seq


#REPEATED RANDOM

def rep_random(a):
    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))
    for _ in range(1,25001):
        sol2 = np.random.choice([np.int64(-1),np.int64(1)], len(a))
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol

def PP_rep_random(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)
    for _ in range(1,25001):
        sol2 = np.random.randint(low=1, high=len(a),size=len(a),dtype=np.int64)
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol




#HILL CLIMBING

def hill_climbing(a):
    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))

    for _ in range(1,25001):
        sol2 = sol[:]
        #generates a random neighbor rather than generating all neighbors and picking one randomly
        sol2[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] = -1 * sol[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] 
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol

def PP_hill_climbing(a):
    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)

    for _ in range(1,25001):
        sol2 = sol[:]
        #generates a random neighbor rather than generating all neighbors and picking one randomly
        sol2[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] = np.random.randint(low=1,high=len(a),dtype=np.int64) 
        if(kk_alg(sol_to_seq(a,sol2)) < kk_alg(sol_to_seq(a,sol))):
            sol = sol2
    return sol




#SIMULATED ANNEALING 

def simul_anneal(a):
    initial_temp=10**10
    cooling_rate=0.8

    sol = np.random.choice([np.int64(-1),np.int64(1)], len(a))

    for t in range(1,25001):
        temp = initial_temp * (cooling_rate**(t/300))

        current_Cost = kk_alg(sol_to_seq(a,sol))

        sol2 = sol[:]
        #generates a random neighbor rather than generating all neighbors and picking one randomly
        sol2[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] = -1 * sol[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] 
        neighbor_Cost = kk_alg(sol_to_seq(a,sol2))

        deltaE =  current_Cost - neighbor_Cost
        prob = np.e **((-deltaE)/temp)

        #if solution is better or if probability says yes to the dress
        if deltaE > 0 or prob > temp: 
            sol = sol2

    return sol         


def PP_simul_anneal(a):
    initial_temp=100
    cooling_rate=0.99

    sol = np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)

    for t in range(1,25001):
        temp = initial_temp * (cooling_rate**t)

        current_Cost = kk_alg(sol_to_seq(a,sol))

        sol2 = sol[:]
        #generates a random neighbor rather than generating all neighbors and picking one randomly
        sol2[np.random.randint(low=1,high=len(a),size=len(a),dtype=np.int64)] = np.random.randint(low=1,high=len(a),dtype=np.int64) 
        neighbor_Cost = kk_alg(sol_to_seq(a,sol2))

        deltaE =  current_Cost - neighbor_Cost
        prob = np.e **((-deltaE)/temp)

        #if solution is better or if probability says yes to the dress
        if deltaE > 0 or prob > temp: 
            sol = sol2

    return sol         


example1 = [10,8,7,6,5]
example1SOL = [1,2,2,4,5]


flag = int(sys.argv[1])
algorithm = int(sys.argv[2])
file = sys.argv[3]
a = extractNumbers(file)

if algorithm == 0:
    kk_alg(a)
elif algorithm == 1:
    rep_random(a)
elif algorithm == 2:
    hill_climbing(a)
elif algorithm == 3:
    simul_anneal(a)
elif algorithm == 11:
    PP_rep_random(a)
elif algorithm == 12:
    PP_hill_climbing(a)
elif algorithm == 13:
    PP_simul_anneal(a)