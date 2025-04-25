import matplotlib.pyplot as plt
import numpy as np
from partition import *
from time import process_time

def randomTests():
    residues = [[] for _ in range(7)]
    runtimes = [[] for _ in range(7)]
    #0 = KK, 1 = RR, 2 = HC, 3 = SIM, 4 = PP_RR, 5 = PP_HC, 6 = PP_HC
    y = np.arange(0,50)

    for _ in range(50):
        seq = np.random.randint(low=1,high=10**12,size=100,dtype=np.int64)
        print(f"Generated seq: {seq}")
        for i in range(7):
            if i == 0:
                begin = process_time()
                residues[0].append(kk_alg(seq))
                runtimes[0].append(process_time()-begin)
                print("Done with kk_alg")
            elif i == 1:
                begin = process_time()
                residues[1].append(eval_sol(seq,rep_random(seq)))
                runtimes[1].append(process_time()-begin)
                print("Done with rep_random")
            elif i == 2:
                begin = process_time()
                residues[2].append(eval_sol(seq,hill_climbing(seq)))
                runtimes[2].append(process_time()-begin)
                print("Done with hill_climbing")
            elif i == 3:
                begin = process_time()
                residues[3].append(eval_sol(seq,simul_anneal(seq)))
                runtimes[3].append(process_time()-begin)
                print("Done with simul_anneal")
            elif i == 4:
                begin = process_time()
                residues[4].append(kk_alg(PP_sol_to_seq(seq,PP_rep_random(seq))))
                runtimes[4].append(process_time()-begin)
                print("Done with PP_rep_random")
            elif i == 5:
                begin = process_time()
                residues[5].append(kk_alg(PP_sol_to_seq(seq,PP_hill_climbing(seq))))
                runtimes[5].append(process_time()-begin)
                print("Done with PP_hill_climbing")
            elif i == 6:
                begin = process_time()
                residues[6].append(kk_alg(PP_sol_to_seq(seq,PP_simul_anneal(seq))))
                runtimes[6].append(process_time()-begin)
                print("Done with PP_simul_anneal")
        print("Done with one round of iterations\n")

    print(f"Average Runtime of KK: {sum(runtimes[0])/50}")
    print(f"Average Runtime of RR: {sum(runtimes[1])/50}")
    print(f"Average Runtime of HC: {sum(runtimes[2])/50}")
    print(f"Average Runtime of SIM: {sum(runtimes[3])/50}")
    print(f"Average Runtime of PP_RR: {sum(runtimes[4])/50}")
    print(f"Average Runtime of PP_HC: {sum(runtimes[5])/50}")
    print(f"Average Runtime of PP_SIM: {sum(runtimes[6])/50}")


    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(1, 7)
    ax1.hist(residues[0], label = "Karmarkar-Karp")
    ax2.hist(residues[1], label = "Repeated Random")
    ax3.hist(residues[2], label = "Hill Climbing")
    ax4.hist(residues[3], label = "Simulated Annealing")
    ax5.hist(residues[4], label = "Prepartioned Repeated Random")
    ax6.hist(residues[5], label = "Prepartitioned Hill Climbing")
    ax7.hist(residues[6], label = "Prepartioned Simulated Annealing")

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
    fig.supylabel('Residue of Generated Set')
    fig.suptitle('Minimal Residues Found by Each Algorithm Over 25000 Iterations')
    fig.set_size_inches(60, 20)
    return residues


randomTests()




