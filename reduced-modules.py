# Very slow partition computing algorithm
def quick_partition(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(sorted(a[:k + 2], reverse=True))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(sorted(a[:k + 1], reverse = True))

# This is the T1 test: it checks if monomials appear dropping an
# exponent by one, but not to 0
def property_check(A,B):
    T1set = B.copy()    # We copy the second set. If an element satisfies the
                        # property we remove it from this set.
    T1 = False

    for (a,b) in B:
        if a>=-b and (a-1,b) in A and a>1:
            T1set.remove((a,b))

        if -b>=a and (a,b+1) in A and b<-1:
            T1set.add((a,b))
            T1set.remove((a,b))

    if len(T1set)==0:   # If this set is empty, the T1 property holds and thus
                        # T1 is true
        T1 = True
    return T1

# This is our main function. We provide it with a Young diagram and it computes
# (as a list of generators) the reduced submodule.
# YD is our Young diagram. G our set of generators and SH is
# the generators for the reduced submodule.
# A monomial corresponds to a point via: x^a y^b <-> (a,-b)

def reduced_module(YD):
    k=len(YD)
    G = {(YD[0],0),(0,-k)}          # The set of generators
    for i in range(1,k):
        if YD[i]<YD[i-1]:
            G.add((YD[i],-i))

    # First we add all true sharp points
    SH = set()

    for i in range(k-1):
        if YD[i]>YD[i+1]:
            SH.add((YD[i]-1,-i))
    SH.add((YD[k-1]-1,-k+1))

    # Next we add pseudo sharp points
    for i in range(1,k-1):
        if YD[i]+1<YD[i-1] and YD[i]==YD[i+1]:
            SH.add((YD[i],-i))

    if YD[0]==YD[1]:
        SH.add((YD[0],0))
    if YD[k-1]>1:
        SH.add((0,-k))

    # Test for Type 1
    T1 = property_check(SH,G)

    # Test for Type 2
    T2 = False
    if T1 == False and len(G.intersection(SH))==0: # Check intersection
        T2 = True

    # Test for Type 3 & 4
    T3 = False
    T4 = False
    if len(G.intersection(SH)) != 0: # If intersection non-emtpy
        G1 = G-SH
        SH1 = SH-G
        T3 = property_check(SH1,G1)
        if T3 == False:
            T4 = True

    return (T1,T2,T3,T4)


# TESTING SUITE:
# Here we apply the code to specific examples.

#print("(T1,T2,T3,T4) = ", reduced_module([4,4,2]))
data = {}
for dim in range(2,40):

    counter1 = 2
    counter2 = 0
    counter3 = 0
    counter4 = 0
    partitions = list(quick_partition(dim))
    no_parts = len(partitions)

    for YD in partitions:
        if len(YD)>1 and YD[0]>1:
            (TEST1,TEST2,TEST3,TEST4) = reduced_module(YD)
            if TEST1 == True:
                counter1+=1
                #print("T1:",*YD)
            if TEST2==True:
                counter2+=1
                #print("T2:",*YD)
            if TEST3 == True:
                counter3+=1
                #print("T3:",*YD)
            if TEST4==True:
                counter4+=1

    p1=round(100*(counter1)/no_parts,2)
    p2=round(100*(counter2)/no_parts,2)
    p3=round(100*(counter3)/no_parts,2)
    p4=round(100*(counter4)/no_parts,2)
    data[dim]=p1,p2,p3,p4

print ("{:<4} {:<10} {:<10} {:<10} {:<10}".format('Dim','T1','T2','T3','T4'))
for dim, c in data.items():
    t1,t2,t3,t4=c
    print ("{:<4} {:<10} {:<10} {:<10} {:<10}".format(dim, t1,t2,t3,t4))
