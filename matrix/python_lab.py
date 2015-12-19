## Task 1
from test.test_iterlen import len
minutes_in_week = 7*24*60

## Task 2
remainder_without_mod = 2304811-47*(2304811//47)

## Task 3
divisible_by_3 = (673+909)%3==0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 1, 10, 20 }
Y1 = { 4, 5, 6 }
{x*y for x in X1 for y in Y1}

## Task 8: enter in the two new sets
X2 = { 0, 1, -1 }
Y2 = { 5 , -5, 2 }
{x*y for x in X2 for y in Y2 if x != y}

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { x for x in range((max(digits)*base**0)+(max(digits)*base**1)+(max(digits)*base**2)+1)}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S if x in T }

## Task 11
L_average = sum([20, 10, 15, 75])/len([20, 10, 15, 75])

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LofL])

## Task 13
cartesian_product = [[a,b] for a in ['A','B','C'] for b in [1,2,3]] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ (a,b,c) for a in S for b in S for c in S if (a+b+c) == 0 ] 

## Task 15
exclude_zero_list = [ (a,b,c) for a in S for b in S for c in S if (a+b+c) == 0 and (a,b,c) != (0,0,0) ] 

## Task 16
first_of_tuples_list = [ (a,b,c) for a in S for b in S for c in S if (a+b+c) == 0 and (a,b,c) != (0,0,0) ][0]

## Task 17
L1 = [1,1,2] # <-- want len(L1) != len(list(set(L1)))
L2 = [2,1] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(100) if x%2!=0}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [ sum(p) for p in zip([10, 25, 40],[1, 15, 20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [p[k] for p in dlist]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [p[k] if k in p else 'NOT PRESENT' for p in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [p[k] if k in p else 'NOT PRESENT' for p in dlist] # <-- as you do here

## Task 23
square_dict = {k:k**2 for k in range(100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {k:k for k in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {d:[min(d//(base**2),max(digits)),
                          min((d-min(d//(base**2),max(digits)) * base**2)//(base),max(digits)),
                          min((d-min(d//(base**2),max(digits)) * base**2-(min((d-min(d//(base**2),max(digits)) * base**2)//(base),max(digits)))*base)//(1),max(digits))] for d in range(1000)}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { names[id]:salary for (id,salary) in d.items() }

## Task 27
def nextInts(L): return [ x + 1 for x in L ]

## Task 28
def cubes(L): return [ x**3 for x in L ] 

## Task 29
def dict2list(dct, keylist): return [ dct[k] for k in keylist ]

## Task 30 
def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist,L) } 

