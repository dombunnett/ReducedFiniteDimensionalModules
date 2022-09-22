from reducedModules import reduced_module, type_tests

# Read the Young diagram as input of form: "4 3 2 1"
# Then it prints the generators and the type.
print("Enter Young diagram in the form: * * ... *")
while True:
    print("> ",end="")
    currentinput = input()
    inputcheck = currentinput.replace(" ","")

    if(currentinput == "exit" or currentinput=="quit"):
        break

    if(inputcheck.isnumeric()):
        YD = list(map(int,currentinput.split()))
        if(all(x>=y for x, y in zip(YD, YD[1:]))):
            if(len(YD)>1 and YD[0]>1):
                (Red,Mod) = reduced_module(YD)
                print("> SH : ", Red)
                print("> Gens : ", Mod)
                print ("> Type : ", type_tests(Red,Mod))
            else:
                print("> Enter more serious Young diagram")
        else:
            print("Ensure sequence is decreasing")
    else:
        print("> Please enter in the correct form, e.g. '4 3 2 1' ")
