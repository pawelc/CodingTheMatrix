# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [p1_v[0] + p1_u[0],p1_v[1] + p1_u[1]]
p1_v_minus_u = [p1_v[0] - p1_u[0],p1_v[1] - p1_u[1]]
p1_three_v_minus_two_u = [3*p1_v[0] - 2*p1_u[0],3*p1_v[1] - 2*p1_u[1]]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [p2_v[0] + p2_u[0],p2_v[1] + p2_u[1],p2_v[2] + p2_u[2]]
p2_v_minus_u = [p2_v[0] - p2_u[0],p2_v[1] - p2_u[1],p2_v[2] - p2_u[2]]
p2_two_v_minus_u = [2*p2_v[0] - p2_u[0],2*p2_v[1] - p2_u[1],2*p2_v[2] - p2_u[2]]
p2_v_plus_two_u = [p2_v[0] + 2*p2_u[0],p2_v[1] + 2*p2_u[1],p2_v[2] + 2*p2_u[2]]



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [0+one,one+one,one+one]
p3_vector_sum_2 = [0+one+one,one+one+one,one+one+one]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.
vecs={'a':[1,1,0,0,0,0,0],'b':[0,1,1,0,0,0,0],'c':[0,0,1,1,0,0,0],'d':[0,0,0,1,1,0,0],'e':[0,0,0,0,1,1,0],'f':[0,0,0,0,0,1,1]}
import itertools
import operator
import functools

def findComb(vecs,vec):
    for i in range(1,len(vecs)+1):
        for comb in itertools.combinations(vecs,i):
            result = [0]*7
            for el in comb:
                result = list(map(lambda tup: tup[0]^tup[1], zip(result,vecs[el])))       
            if vec == result:
                return set(comb)
    return {}
print(findComb(vecs, [0,0,1,0,0,1,0]))
u_0010010 = {'c', 'e', 'd'}
print(findComb(vecs, [0,1,0,0,0,1,0]))
u_0100010 = {'c', 'b', 'e', 'd'}



## Problem 5
# Use the same format as the previous problem
vecs={'a':[1,1,1,0,0,0,0],'b':[0,1,1,1,0,0,0],'c':[0,0,1,1,1,0,0],'d':[0,0,0,1,1,1,0],'e':[0,0,0,0,1,1,1],'f':[0,0,0,0,0,1,1]}
print(findComb(vecs, [0,0,1,0,0,1,0]))
v_0010010 = {'c', 'd'}
print(findComb(vecs, [0,1,0,0,0,1,0]))
v_0100010 = set()

import math

def dot(veca,vecb):
    return sum(map(lambda el: el[0]*el[1],zip(veca,vecb)))
## Problem 6
uv_a = dot([1,0],[5,4321])
uv_b = dot([0,1],[12345,6])
uv_c = dot([-1,3],[5,7])
uv_d = dot([-math.sqrt(2)/2,math.sqrt(2)/2],[math.sqrt(2)/2,-math.sqrt(2)/2])


## Problem 7
# use 'one' instead of '1'
x_gf2 = [one,0,0,0]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

