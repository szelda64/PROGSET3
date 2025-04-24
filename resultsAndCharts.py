import matplotlib.pyplot as plt
import numpy as np
from partition import *

def randomTests():
    residues = [[] for _ in range(7)]
    #0 = KK, 1 = RR, 2 = HC, 3 = SIM, 4 = PP_RR, 5 = PP_HC, 6 = PP_HC
    y = np.arange(0,50)

    for _ in range(50):
        a = np.random.randint(low=1,high=100,size=100,dtype=np.int64)

        for i in range(7):
            if i == 0:
                residues[0].append(kk_alg(a))
            elif i == 1:
                residues[1].append(eval_sol(a,rep_random(a)))
            elif i == 2:
                residues[2].append(eval_sol(a,hill_climbing(a)))
            elif i == 3:
                residues[3].append(eval_sol(a,simul_anneal(a)))
            elif i == 4:
                residues[4].append(kk_alg(PP_sol_to_seq(a,PP_rep_random(a))))
            elif i == 5:
                residues[5].append(kk_alg(PP_sol_to_seq(a,PP_hill_climbing(a))))
            elif i == 6:
                residues[6].append(kk_alg(PP_sol_to_seq(a,PP_simul_anneal(a))))

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(y,residues[0],label="Karmarkar-Karp") 
    ax1.plot(y,residues[1],label="Repeated Random") 
    ax1.plot(y,residues[2],label="Hill-Climbing") 
    ax1.plot(y,residues[3],label="Simulated Anneal") 

    ax2.plot(y,residues[0],label="Karmarkar-Karp") 
    ax2.plot(y,residues[4],label="Repeated Random") 
    ax2.plot(y,residues[5],label="Hill-Climbing") 
    ax2.plot(y,residues[6],label="Simulated Anneal") 


    ax1.legend()
    ax2.legend()
    fig.supxlabel('Run Number')
    fig.supylabel('Residue')
    fig.suptitle('Residues of Algorithms')

    fig.set_size_inches(18.5, 8.5)
    fig.show()
randomTests()




