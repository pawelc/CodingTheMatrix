# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vec import Vec
from vecutil import zero_vec, list2vec
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[   1,2,0,2,0   ],
                  [   0,1,0,3,4   ],
                  [   0,0,2,3,4  ],
                  [   0,0,0,2,0   ],
                  [   0,0,0,0,4   ]]

echelon_form_2 = [[   0,4,3,4,4   ],
                  [   0,0,4,2,0   ],
                  [   0,0,0,0,1   ],
                  [   0,0,0,0,0   ]]

echelon_form_3 = [[   1,0,0,1   ],
                  [   0,0,0,1   ],
                  [   0,0,0,0   ]]

echelon_form_4 = [[   1,0,0,0   ],
                  [   0,1,0,0   ],
                  [   0,0,0,0   ],
                  [   0,0,0,0   ]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    col_non_zero_idx = -1
    for row in A:
        l=list(map(lambda el : el!=0,row))
        non_zero_idx=l.index(True) if True in l else len(row)
        if non_zero_idx == len(row) or non_zero_idx > col_non_zero_idx:
            col_non_zero_idx = non_zero_idx
        else:
            return False
    return True

#is_echelon([[1,1,1],[0,1,1],[0,0,1]])
#is_echelon([[0,1,1],[0,1,0],[0,0,1]])
#M1 = [[0,0,0],[0,0,0],[0,0,0]]
#M2 = [[1,0,0],[0,1,0],[0,1,0]]
#M3 = [[0]*4,[1]*4]
#M4 = [[1,0,0,0,0,0,0,0],
#       [0,1,1,1,1,1,1,1],
#       [0,0,1,1,1,0,1,0],
#      [0,0,0,0,0,1,1,0]]
#M5 = [[1]]
#M6 = [[0]]
#[is_echelon(M) for M in [M1, M2, M3, M4, M5, M6]]


## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for i,row in enumerate(reversed(rowlist)):
        l=list(map(lambda el : el!=0,[row[c] for c in label_list]))
        non_zero_idx=l.index(True) if True in l else len(label_list)
        if non_zero_idx == len(label_list):
            continue
        x[label_list[non_zero_idx]] = (b[len(b)-i-1] - x*row)/row[label_list[non_zero_idx]]
    return x

#D = {'A','B','C','D','E'}
#U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
#b_list = [one,0,one]
#cols = ['A', 'B', 'C', 'D', 'E']
#echelon_solve(U_rows, cols, b_list)
#
#cols = ['A', 'B', 'C', 'D', 'E']
#D = set(cols)
#U_rows = [Vec(D, {'A':one, 'C':one}), Vec(D, {'C':one, 'E':one}), Vec(D,{'D':one})]
#b_list = [one, one, one]
#u = echelon_solve(U_rows, cols, b_list)


## Problem 6
D = {'A','B','C','D'}
rowlist = [Vec(D, {'A':one, 'B':one,'D':one}), Vec(D, {'B':one}), Vec(D,{'C':one}),Vec(D,{'D':one})]    # Provide as a list of Vec instances
label_list = sorted(list(D)) # Provide as a list
b = [ one,one,0,0 ]          # Provide as a list
#x=echelon_solve(rowlist, label_list, b)


## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
def project_par(a,b): return list2vec(a)*list2vec(b)/(list2vec(a)*list2vec(a))*list2vec(a)

def project_ort(a,b): return list2vec(b)-project_par(a, b)

#project_par([-3,-2,-1,4],[7,2,5,0])

closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list

project_onto_1=[project_par([3,0],[2,1]).f[i] for i in range(2)]
projection_orthogonal_1=[project_ort([3,0],[2,1]).f[i] for i in range(2)]

project_onto_2=[project_par([1,2,-1],[1,1,4]).f[i] for i in range(3)]
projection_orthogonal_2=[project_ort([1,2,-1],[1,1,4]).f[i] for i in range(3)]

project_onto_3=[project_par([3,3,12],[1,1,4]).f[i] for i in range(3)]
projection_orthogonal_3=[project_ort([3,3,12],[1,1,4]).f[i] for i in range(3)]

import math
def norm(v): return math.sqrt(sum(map(lambda x:x**2,v)))
## Problem 11
norm1 = norm([2,2,1])
norm2 = norm([math.sqrt(2),math.sqrt(3),math.sqrt(5),math.sqrt(6)])
norm3 = 1

