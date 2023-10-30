import numpy as np

def compute_G(x,n):
    g = 0
    for j in range(0,N):
        g = g + x[j]*x[(j+n)%N]
    return g/N

def MCaverage(x,G):
    for j in range(0,N): # initialize x
        x[j] = 0
    for j in range(0,5*N_cor): # thermalize x
        update(x)
    for alpha in range(0,N_cf): # loop on random paths
        for j in range(0,N_cor):
            update(x)
        for n in range(0,N):
            G[alpha][n] = compute_G(x,n)
    for n in range(0,N): # compute MC averages
        avg_G = 0
        for alpha in range(0,N_cf):
            avg_G = avg_G + G[alpha][n]
        avg_G = avg_G/N_cf
        print "G(%d) = %g" % (n,avg_G)

x = np.arange(0,2,0.05)
