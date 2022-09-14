from reducedModules import reduced_module

#YD = list(map(int,input("Enter Young diagram: ").split()))
YD = [4,2,2,1]
(SH,G) = reduced_module(YD)

print(G)
print(SH)

pic=[]

for i in range(len(YD)):
    pic.append("_|" * YD[i])

print(*pic,sep="\n")
