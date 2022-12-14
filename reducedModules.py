# This is the T1 test: it checks if monomials appear dropping the
# larger exponent by one, but not to 0
def property_check(A,B):
    T1set = B.copy()    # We copy the second set. If an element satisfies the
                        # property we remove it from this set.
    T1 = 0

    for (a,b) in B:
        if a>=-b and (a-1,b) in A and a>1:
            T1set.remove((a,b))

        if -b>=a and (a,b+1) in A and b<-1:
            T1set.add((a,b))
            T1set.remove((a,b))

    if len(T1set)==0:   # If this set is empty, the T1 property holds and thus
                        # T1 is true
        T1 = 1
    return T1

# This is our main function. We provide it with a Young diagram and it computes
# (as a list of generators) the reduced submodule.
#
# YD is our Young diagram. G our set of generators and SH is the generators for
# the reduced submodule. A monomial corresponds to a point via:
#  x^a y^b <-> (a,-b)

def reduced_module(YD):
    k=len(YD)
    G = {(YD[0],0),(0,-k)}          # The set of generators
    for i in range(1,k):
        if YD[i]<YD[i-1]:
            G.add((YD[i],-i))

    SH = set()                      # First we add all true sharp points

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
    return (SH,G)

# TYPE TEST
# The following function tests for the type of the module.
# It takes as input the module and the reduced submodule.

def type_tests(SH,G):               # Test for Types
    T1 = property_check(SH,G)       # Type 1
    T2 = 0
    if T1 == 0 and len(G.intersection(SH))==0: # Check intersection
        T2 = 1
    T3 = 0                      # Test for Type 3 & 4
    T4 = 0
    if len(G.intersection(SH)) != 0: # If intersection non-emtpy
        G1 = G-SH
        SH1 = SH-G
        T3 = property_check(SH1,G1)
        if T3 == 0:
            T4 = 1

    return [T1,T2,T3,T4]
