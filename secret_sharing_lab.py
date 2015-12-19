# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from solver import solve
from vec import Vec
from matutil import listlist2mat, rowdict2mat
from independence import rank,is_independent
from itertools import combinations



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])



def choose_secret_vector(s,t):
    return solve(rowdict2mat({i:v for (i,v) in enumerate([a0,b0] + [ vec for vec in [Vec(range(len(a0.D)),{i:randGF2() for i in range(len(a0.D))}) for _ in range(len(a0.D)-2)]])}), list2vec([s,t] + [randGF2() for _ in range(len(a0.D)-2)]))


## Problem 2
# Give each vector as a Vec instance
secret_a0=a0
secret_b0=b0
rest=[]

while True:
    rest=[Vec(set(range(len(a0.D))),{i:randGF2() for i in range(len(a0.D))}) for _ in range(8)]
    vecs=[(secret_a0, secret_b0),(rest[0],rest[1]),(rest[2],rest[3]),(rest[4],rest[5]),(rest[6],rest[7])]
    if all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
        break


secret_a1=rest[0]
secret_b1=rest[1]
secret_a2=rest[2]
secret_b2=rest[3]
secret_a3=rest[4]
secret_b3=rest[5]
secret_a4=rest[6]
secret_b4=rest[7]

