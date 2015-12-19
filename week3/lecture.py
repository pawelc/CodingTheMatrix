[[0]*4]*3

[[0 for _ in range(4)] for _ in range(3)]

[[i for i in range(j,j+3)] for j in range(0,-4,-1)]

[[i-j for i in range(3)] for j in range(4)] 

def identity(D): return Mat((D,D), { (e,e):1 for e in D })

def mat2coldict(A): return {c: Vec(A.D[0],{r:A[r,c] for r in A.D[0]}) for c in A.D[1] }

def transpose(M): return Mat((M.D[1],M.D[0]),{(c,r):M[r,c] for r in M.D[0] for c in M.D[1]})