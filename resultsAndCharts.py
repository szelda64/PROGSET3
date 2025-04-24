import matplotlib.pyplot as plt
import numpy as np
from partition import *

def randomTests():
    residues = [[] for _ in range(7)]
    #0 = KK, 1 = RR, 2 = HC, 3 = SIM, 4 = PP_RR, 5 = PP_HC, 6 = PP_HC
    y = np.arange(0,50)

    for _ in range(50):
        seq = sol = np.random.randint(low=1,high=10**12,size=100,dtype=np.int64)
        print(f"Generated seq: {seq}")
        for i in range(7):
            if i == 0:
                residues[0].append(kk_alg(seq))
                print("Done with kk_alg")
            elif i == 1:
                residues[1].append(eval_sol(seq,rep_random(seq)))
                print("Done with rep_random")
            elif i == 2:
                residues[2].append(eval_sol(seq,hill_climbing(seq)))
                print("Done with hill_climbing")
            elif i == 3:
                residues[3].append(eval_sol(seq,simul_anneal(seq)))
                print("Done with simul_anneal")
            elif i == 4:
                residues[4].append(kk_alg(PP_sol_to_seq(seq,PP_rep_random(seq))))
                print("Done with PP_rep_random")
            elif i == 5:
                residues[5].append(kk_alg(PP_sol_to_seq(seq,PP_hill_climbing(seq))))
                print("Done with PP_hill_climbing")
            elif i == 6:
                residues[6].append(kk_alg(PP_sol_to_seq(seq,PP_simul_anneal(seq))))
                print("Done with PP_simul_anneal")
        print("Done with one round of iterations")
    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(1, 7)
    ax1.plot(y, residues[0], label = "Karmarkar-Karp")
    ax2.plot(y, residues[1], label = "Repeated Random")
    ax3.plot(y, residues[2], label = "Hill Climbing")
    ax4.plot(y, residues[3], label = "Simulated Annealing")
    ax5.plot(y, residues[4], label = "Prepartioned Repeated Random")
    ax6.plot(y, residues[5], label = "Prepartitioned Hill Climbing")
    ax7.plot(y, residues[6], label = "Prepartioned Simulated Annealing")

    ax1.set_title('Minimal Residues Found by Karmarkar-Karp over 25000 iterations')
    ax2.set_title('Minimal Residues Found by Repeated Random over 25000 iterations')
    ax3.set_title('Minimal Residues Found by Hill Climbing over 25000 iterations')
    ax4.set_title('Minimal Residues Found by Simulated Annealing over 25000 iterations')
    ax5.set_title('Minimal Residues Found by PP-Repeated Random over 25000 iterations')
    ax6.set_title('Minimal Residues Found by PP-Hill Climbing over 25000 iterations')
    ax7.set_title('Minimal Residues Found by PP-Simulated Annealing over 25000 iterations')
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    ax5.legend()
    ax6.legend()
    ax7.legend()
    fig.supxlabel('Set #')
    fig.supylabel('Residue of Generated Set')
    fig.suptitle('Minimal Residues Found by Each Algorithm Over 25000 Iterations')
    fig.set_size_inches(60, 20)
    return residues

    





