class Vec:
    def __init__(self,labels,function):
        self.D = labels
        self.f = function

def zero_vec(D): return Vec(D, dict(zip(D,[0]*len(D))))

zv=zero_vec({'A','B'})
zv.D
zv.f