import numpy as np
from reducedModules import reduced_module
from reducedModules import type_tests
from partitions import quick_partition

# Read the Young diagram as input of form: "4 3 2 1"
# Then it prints the generators and the type.
Young_Diagram = list(map(int,input("Enter Young diagram: ").split()))
if(len(Young_Diagram)>1):
    (Red,Mod) = reduced_module(Young_Diagram)
    print(Red,Mod)
    print (type_tests(Red,Mod))
else:
    print("Nonsense detected, compute it yourself! Moving on...")

# Next we compute for all modules of all dimensions up to a maximum.
# One enters the maximum dimension to be considered and the name of
# the file under which to save the data.
max_dim = int(input("Enter the maximum dimension to be tested: "))
name = str(input("Name file to save data under: "))
data = {}                               # Here we store all data computed
for dim in range(2,max_dim+1):          # Loop over all dimensions
    counter = np.array([2,0,0,0])
    partitions = list(quick_partition(dim)) # Compute the partitions
    N = len(partitions)                     # How many partitions?

    for YD in partitions:                   # Loop over all YDs of that
        if len(YD)>1 and YD[0]>1:           # dimension.
            (SH,G) = reduced_module(YD)     # Compute reduced module
            types = type_tests(SH,G)        # Compute its types
            if(types == [0,0,0,0]):         # Check for impossible behaviour
                print("PROBELM")
                break
            counter = np.add(types,counter) # Add to counter.
                                            # Compute distribution for that
                                            # dimension in %.
    data[dim] = tuple(round(100*(counter[i])/N,2) for i in range(4))

# We write the data computed to the file named above.
f = open(name + ".txt","x")
f.write("{:<4} {:<10} {:<10} {:<10} {:<10}".format('Dim','T1','T2','T3','T4'))
for dim, c in data.items():
    t1,t2,t3,t4=c
    f.write("\n")
    f.write("{:<4} {:<10} {:<10} {:<10} {:<10}".format(dim, t1,t2,t3,t4))
f.close()
