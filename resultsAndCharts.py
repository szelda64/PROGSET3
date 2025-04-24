import matplotlib.pyplot as plt
import numpy as np
from partition import *

def randomTests():
    residues = [[] for _ in range(7)]
    #0 = KK, 1 = RR, 2 = HC, 3 = SIM, 4 = PP_RR, 5 = PP_HC, 6 = PP_HC

    for _ in range(50):
        seq = sol = np.random.randint(low=1,high=100,size=100,dtype=np.int64)

        for i in range(7):
            if i == 0:
                residues[0].append(kk_alg(a))
            elif i == 1:
                residues[1].append(rep_random(a))
            elif i == 2:
                residues[2].append(hill_climbing(a))
            elif i == 3:
                residues[3].append(simul_anneal(a))
            elif i == 4:
                residues[4].append(PP_rep_random(a))
            elif i == 5:
                residues[5].append(PP_hill_climbing(a))
            elif i == 6:
                residues[6].append(PP_simul_anneal(a))

    





