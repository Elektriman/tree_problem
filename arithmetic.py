# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:59:46 2021

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt

Triples = [(3, 4, 5), (20, 21, 29), (11, 60, 61), (13, 84, 85),
           (5, 12, 13), (12, 35, 37), (16, 63, 65), (36, 77, 85), 
           (8, 15, 17), (9, 40, 41), (33, 56, 65), (39, 80, 89),
           (7, 24, 25), (28, 45, 53), (48, 55, 73), (65, 72, 97)]

#crible d'hérathosthène
def crible(n):
    C = np.full(n, True)
    C[:2] = False
    l = int(np.sqrt(n))
    i = 2
    while i<=l :
        if C[i] :
            for u in range(2*i,n,i):
                C[u]=False
        i+=1
    return(C)

def decomposition(n):
    C = np.arange(n)[crible(n)]
    fact = {2:0}
    N = n
    while N != 1 :
        if N%(C[len(fact)-1])==0 :
            N //= C[len(fact)-1]
            fact[C[len(fact)-1]]+=1
        else :
            fact[C[len(fact)-1]]=0
    return fact

def PGCD(a,b):
    Da = decomposition(a)
    Db = decomposition(b)
    m = max([i for i,j in {**Da, **Db}.items()])
    C = np.arange(m)[crible(m)]
    
    l = []
    for i in range(min(len(Da), len(Db))):
        if Da[C[i]]*Db[C[i]]>0 :
            l.append(C[i])
    return np.prod(np.array(l))

def PPCM_(a, b):
    return int(a*b / PGCD(a, b))

def PPCM(*args):
    if len(args)==2 :
        return PPCM_(args[0], args[1])
    else :
        return PPCM(PPCM(args[0], args[1]), *args[2:])

def plot_hex(a,b,c):
    X = [0,a,a+c,2*a+c,a+c,a,0]
    Y = [b,0,0,b,2*b,2*b,b]
    
    X = list(map(lambda x:x-(a+c/2), X))
    Y = list(map(lambda x:x-b, Y))
    
    colour = (c/97, 150/255, 150/255)
    
    plt.plot(X,Y, c=colour)
    plt.axis('equal')
    plt.show()

def dumb_ppcm(n,p):
    if n>p :
        return dumb_ppcm(p,n)
    elif p/n == float(p//n) :
        return p
    else :
        i,j = 1,1
        while i*p!=j*n :
            if i*p > j*n :
                j+=1
            else :
                i+=1
        return(i*p)

if __name__ == '__main__' :
    
    # T = np.array(Triples)
    # ppcm = PPCM(*tuple(T[:,2]))
    # V = np.full(len(T), 720720)//T[:,0]
    # X = np.zeros(len(T))
    # X = T[:,1]*V
    
    # X = np.hstack((np.array([0,0]), X))
    # Y = np.array([0, 720720]+[0]*len(T), dtype=np.uint64)
    
    # plt.scatter(X,Y)
    
    # for t in Triples :
    #     plot_hex(*t)
    
    print(dumb_ppcm(12,16))
    print(PPCM(12,16))
