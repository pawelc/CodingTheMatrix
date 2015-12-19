from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
import math
import itertools

import echelon
from random import randint
from timeit import itertools

def root_method(N):
    for a in range(math.ceil(math.sqrt(N)),N):
        b=math.sqrt(a**2-N)
        if b==int(b):
            return (a-b,a+b)
    return None

def gcd(x,y): return x if y == 0 else gcd(y, x % y)
#
#r=randint(10000,1000000000)
#s=randint(10000,1000000000)
#t=randint(10000,1000000000)
#
#a=r*s
#b=s*t
#
#d=gcd(a,b)
#
#a%d==0
#b%d==0
#d>=s

#print(root_method(118))
#
#for i in range(100):
#    print("%d solved to %s"%(i,root_method(i)))

#N=367160330145890434494322103
#a=67469780066325164
#b=9429601150488992
#
#(a * a - b * b) % N == 0
#
#N%gcd(a-b,N) == 0

#dumb_factor(75, {2,3,5,7})

#primeset={2,3,5,7,11,13}
#x=12
#dumb_factor(x, primeset)


#    
## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return 0 if i%2==0 else one

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset,{f:int2GF2(i) for (f,i) in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = [] 
    rowlist = []
    for x in itertools.count(intsqrt(N)+2):
        b=x**2-N
        factors=dumb_factor(b, primeset)
        if len(factors)>0:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
            if len(roots) >= len(primeset)+1:
                break
    return roots,rowlist

N=2419
#find_candidates(N, primes(32))
a = 53*77
b = 2*3**2*5*13
d=gcd(a-b,N)
N%d==0

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist=[roots[i] for i,f in v.f.items() if f==one]
    a=prod(alist)
    c=prod([x*x-N for x in alist])
    b=intsqrt(c)    
    assert b*b == c
    return (a,b) 

#v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: one, 2: one, 4: 0, 5: one, 11: one})
#N = 2419
#roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
#find_a_and_b(v, roots, N)

## Task 5
#N=2461799993978700679
#primelist=primes(10000)
#roots,rowlist=find_candidates(N, primelist)
#M=echelon.transformation_rows(rowlist)
#v=M[len(M)-2]
#a,b=find_a_and_b(v, roots, N)
#d=gcd(a-b,N)
#d!=1
#d!=N

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561 
