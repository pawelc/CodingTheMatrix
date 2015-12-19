# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [n for n in L if n % num != 0]

myFilter([1,2,4,5,7],2)



## Problem 2
def myLists(L): return [list(range(1,n+1)) for n in L]



## Problem 3
def myFunctionComposition(f, g): return {k:g[v] for (k,v) in f.items()}

myFunctionComposition({0:'a', 1:'b'},{'a':'apple', 'b':'banana'})

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (3+1j)+(2+2j)
complex_addition_b = (-1+2j)+(1-1j)
complex_addition_c = (2+0j)+(-3+.001j)
complex_addition_d = 4*(0+2j)+(.001+1j)


## Problem 5
GF2_sum_1 = 1 if True^True^True^False else 0
GF2_sum_2 = 1 if True&True^False&True^False&False^True&True else 0
GF2_sum_3 = 1 if (True^True^True)&(True^True^True^True) else 0


## Problem 6
def mySum(L): 
    current=0
    for n in L:
        current += n
    return current



## Problem 7
def myProduct(L):
    current=1
    for n in L:
        current *= n
    return current



## Problem 8
def myMin(L):
    current=None
    for n in L:
        if current is None or current > n:
            current = n
    return current



## Problem 9
def myConcat(L):
    current=''
    for n in L:
        current += n
    return current



## Problem 10
def myUnion(L):
    current=L[0] if len(L)>0 else set()
    for s in L:
        current |= s
    return current

