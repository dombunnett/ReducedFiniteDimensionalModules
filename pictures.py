from reducedModules import reduced_module
from reducedModules import type_tests

#YD = list(map(int,input("Enter Young diagram: ").split()))
YD = [10,7,7,6,5,5,5,2,2,2,2,1]
(SH,G) = reduced_module(YD)


print("G = ", G)
print("SH = ", SH)
print(type_tests(SH,G))

print("-"*(2*YD[0])) # Line fill for clarity

picA={}         # Will be original Young diagram
picB={}         # With reduced module
picC={}         # The complement of the two

# Makes and prints the original Yound diagram
for i in range(len(YD)):
    picA[i] = "_|" * YD[i] + "   "
for i in range(len(YD)):
    print(picA[i])

print("-"*(2*YD[0])) # Line fill for clarity

# Makes and prints with the reduced module generators shown

S = set(range(0,len(YD)))

for (a,b) in SH:
    picB[-b] = picA[-b][0:2*a] + "*" + picA[-b][(2*a)+1]
    if(picB[-b].count("*|") == 0):
        picC[-b] = "  "
    else:
        picC[-b] = "  "*((YD[-b]-1))  + "|*|"
    S.remove(-b)
for b in S:
    picB[b] = picA[b]
    picC[b] = ""

for i in range(len(YD)):
    print(picB[i])

print("-"*(2*YD[0])) # Line fill for clarity

for i in range(len(YD)):
    print(picC[i])
