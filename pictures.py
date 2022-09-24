from reducedModules import reduced_module, type_tests

def make_pictures(YD):
    (SH,G) = reduced_module(YD)

    print("Type = ",type_tests(SH,G))

    print("-"*(2*YD[0])) # Line fill for clarity

    picA={}         # Will be original Young diagram.
    picB={}         # With reduced module.
    picC={}         # The complement of the two.

    # Makes and prints the original Yound diagram
    for i in range(len(YD)):
        picA[i] = "_|" * YD[i] + "  "      # Empty spaces for latter use
    for i in range(len(YD)):
        print(picA[i])
    picA[len(YD)] = "  "
    print(" ")
    print("-"*(2*YD[0])) # Line fill for clarity

    # Makes and prints with the reduced module generators shown

    S = set(range(0,len(YD)))       # We make a measure of the rows of the YD
                                    # without SH and define them after.
    for (a,b) in SH:
        picB[-b] = picA[-b][0:2*a] + "*" + picA[-b][(2*a)+1]
        if(picB[-b].count("*|") == 0):
            picC[-b] = "  "
        else:
            picC[-b] = "  "*((YD[-b]-1))  + "|*|"
        if(a>0):
            S.remove(-b)
        if(a==0 and b==-len(YD)+1):
            S.remove(-b)

    if(YD[len(YD)-1]>1):
        picB[len(YD)] = "*"
    else:
        picB[len(YD)-1] = "*|"
        picB[len(YD)] = ""
        picC[len(YD)] = ""

    for b in S:
        picB[b] = picA[b]
        picC[b] = ""


    for i in range(len(YD) + 1):
        print(picB[i])

    print("-"*(2*YD[0])) # Line fill for clarity

    for i in range(len(YD) + 1):
        print(picC[i])

print("Enter Young diagram in the form: * * ... *")
while True:
    print("> ",end="")
    currentinput = input()
    inputcheck = currentinput.replace(" ","")   # Remove spaces to check input
                                                # format
    if(currentinput == "exit" or currentinput=="quit"): # to exit program
        break

    if(inputcheck.isnumeric()):                    # Check is numbers
        YD = list(map(int,currentinput.split()))
        if(all(x>=y for x, y in zip(YD, YD[1:]))): # Checks decreasing sequence
            if(len(YD)>1):
                make_pictures(YD)
            else:
                print("> Enter more serious Young diagram")
        else:
            print("> Ensure sequence is decreasing")
    else:
        print("> Please enter in the correct form, e.g. '4 3 2 1' ")
