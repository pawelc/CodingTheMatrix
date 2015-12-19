from orthogonalization import orthogonalize
from orthogonalization import aug_orthogonalize
from vec import Vec
from vecutil import list2vec
from matutil import coldict2mat

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [v/(v*v)**0.5 for v in orthogonalize(L)]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Qlist,Rlist=aug_orthogonalize(L)
    scale=[(Qlist[i]*Qlist[i])**0.5 for i,v in enumerate(Rlist)]
    Rlist = [adjust(v,scale) for v in Rlist]
    Qlist=orthonormalize(Qlist)
    return (Qlist,Rlist)

def adjust(v,multipliers):
    w=v.copy()
    for i,m in enumerate(multipliers):
        w[i] = v[i] * m
    return w


#L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
#print(coldict2mat(L))
#Qlist, Rlist = aug_orthonormalize(L)
#print(coldict2mat(Qlist))
#print(coldict2mat(Rlist))
#print(coldict2mat(Qlist)*coldict2mat(Rlist))
#print(coldict2mat(Qlist)*coldict2mat(Rlist)-coldict2mat(L))