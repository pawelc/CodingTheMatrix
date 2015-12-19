3j

L=[2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j]
from plotting import plot
plot(L)

import os
os.getcwd()
os.chdir('/Users/pawelc/Google Drive/git/projects/Coding the Matrix')

from image import *
I=color2gray(file2image('guffy.png'))
r=len(I)
c=len(I[0])
M=[x+y*1j for x in range(c) for y in range(r) if I[r-y-1][x] < 120]
plot(M,max(r,c),1)
abs(1+1j)
plot({z+(1+2j) for z in L})
plot([z - (c/2+(r/2)*1j) for z in M], max(r,c),1)
plot({0.5*z for z in L})

from math import e,pi
plot([e**(t*2*pi*1j/20) for t in range(20)])
[i for i in range(20)]
plot([2*e**(t*2*pi*1j/20) for t in range(20)])

plot([e**(pi*1j/4)*z for z in L])

from GF2 import one
one+one
one*one
one*0
one/one


def encrypt(p,k): return p+k

k = one
p = one
c = encrypt(p, k)
c

1e16 + 1

[x,y,z] = [4*1, 4*2, 4*3]

def twice(z): return 2*z

twice('Paw')

import math
math.pow(math.sqrt(3),2)
math.sqrt(-1)
math.cos(math.pi)
math.log(math.e)

from random import randint
randint(0,10)
def movie_review(name): return "See it" if randint(0,1) == 1 else "A gem" if randint(0,1)==1 else "Claptrap"

movie_review('lal')