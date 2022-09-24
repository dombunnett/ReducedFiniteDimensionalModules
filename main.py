from reducedModules import reduced_module, type_tests

# Read the Young diagram as input of form: "4 3 2 1"
# Then it prints the generators and the type.
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
            if(len(YD)>1 and YD[0]>1):
                (Red,Mod) = reduced_module(YD)
                print("> Generators of M : ", Mod)
                print("> R(M) generators : ", Red)
                print("> Type : ", type_tests(Red,Mod))
            else:
                print("> Enter more serious Young diagram")
        else:
            print("Ensure sequence is decreasing")
    else:
        print("> Please enter in the correct form, e.g. '4 3 2 1' ")
