def calc(argv):
    operation = 0
    suma = 0
    mult = 1
    counter = 0

    for arg in argv:

        # counter control the flow
        if (counter == 0):
            
            # Add modes if needed, longer optcode needs to be trimmed
            modeParam = [0, 0, 0]
            if (len(str(arg)) == 4):
                modeParam[0] = int(str(arg)[0])
                modeParam[1] = int(str(arg)[1])
                arg = int(str(arg)[2:])

            elif (len(str(arg)) == 3):
                modeParam[0] = int(str(arg)[0])
                arg = int(str(arg)[1:])

            # determine operation
            if (arg == 1):
                operation = 1
                counter = 3
                suma = 0
                
            elif (arg == 2):
                operation = 2
                counter = 3
                mult = 1

            elif (arg == 3):
                operation = 3
                counter = 1
            
            elif (arg == 4):
                operation = 4
                counter = 1
            
            elif (arg == 99):
                #print("Exit")
                return argv

        else:
            # adding
            if (operation == 1):
                if (counter >= 2):
                    
                    # Handling mode in addition
                    if (counter == 3):
                        if (modeParam[0] == 0):
                            suma += argv[arg]
                        else:
                            suma += arg
                    elif (counter == 2):
                        suma += argv[arg] if modeParam[1] == 0 else arg

                elif (counter == 1):
                    print("Suma: ",suma)
                    print("arg: ",arg)
                    print("Mode: ", modeParam)
                    argv[arg] = suma

            # multiplication
            elif (operation == 2):
                if (counter >= 2):
                    
                    # Handling mode in multiplication
                    if (counter == 3):
                        mult *= argv[arg] if modeParam[0] == 0 else arg
                    elif (counter == 2):
                        mult *= argv[arg] if modeParam[1] == 0 else arg

                elif (counter == 1):
                    argv[arg] = mult

            # take input
            elif (operation == 3):
                argv[arg] = int(input("Input: "))

            # give output
            elif (operation == 4):
                print("Output: ", argv[arg])
            
            counter -= 1
    
    return argv


if __name__ == "__main__":

    first = [1,0,0,0,99]
    print(calc(first))
    
    second = [2,3,0,3,99]
    print(calc(second))

    third = [2,4,4,5,99,0]
    print(calc(third))

    fourth = [1,1,1,4,99,5,6,0,99]
    print(calc(fourth))

    #fifth = [3,0,4,0,99]
    #print(calc(fifth))

    puzzle_input = [3,225,1,225,6,6,1100,1,238,2125,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
    print(len("calc_here"))
    modeParam = [0, 0, 0]
    print("Answer: ", calc(puzzle_input))