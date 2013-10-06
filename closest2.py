
def closestpair2(L):
    def square(x): return x*x
    def sqdist(p,q): return square(p[0]-q[0])+square(p[1]-q[1])
    

    best = [sqdist(L[0],L[1]), (L[0],L[1])]
    
    # check whether pair (p,q) forms a closer pair than one seen already
    def testpair(p,q):
        d = sqdist(p,q)
        if d < best[0]:
            best[0] = d
            best[1] = p,q
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            testpair(L[i],L[j])     

    return best[1]

#ans = closestpair2([(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),\
#              (19,7),(14,22),(8,19),(7,29),(10,11),(1,13)])

#print ans
